import sys
import importlib
import types
from importlib.machinery import ModuleSpec

# Patch rules library to avoid KeyError on duplicate registrations in test environment
import rules.rulesets
original_add_rule = rules.rulesets.RuleSet.add_rule

def patched_add_rule(self, name, pred):
    try:
        original_add_rule(self, name, pred)
    except KeyError:
        pass

rules.rulesets.RuleSet.add_rule = patched_add_rule


class AliasFinder:
    @classmethod
    def find_spec(cls, fullname, path=None, target=None):
        for old_prefix, new_prefix in [('pretix', 'eventyay'), ('pretalx', 'eventyay'), ('venueless', 'eventyay')]:
            if fullname == old_prefix or fullname.startswith(old_prefix + '.'):
                new_name = fullname.replace(old_prefix, new_prefix, 1)
                try:
                    # Import the real eventyay module (it executes and registers things correctly once)
                    mod = importlib.import_module(new_name)
                    
                    class AliasLoader:
                        def create_module(self, spec):
                            # Create a new module object for the alias to prevent renaming the real module
                            alias_mod = types.ModuleType(spec.name)
                            alias_mod.__dict__.update(mod.__dict__)
                            alias_mod.__name__ = spec.name
                            return alias_mod
                        def exec_module(self, module):
                            pass
                            
                    return ModuleSpec(
                        fullname, 
                        AliasLoader(), 
                        is_package=getattr(mod, '__path__', None) is not None
                    )
                except ImportError:
                    pass
        return None

sys.meta_path.insert(0, AliasFinder)
