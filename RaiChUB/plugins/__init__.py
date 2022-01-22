import sys
from os.path import dirname
from typing import List
import time

def __list_all_modules():
    from os.path import dirname, basename, isfile
    import glob
    # This generates a list of modules in this folder for the * in __main__ to work.
    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [basename(f)[:-3] for f in mod_paths if isfile(f)
                   and f.endswith(".py")
                   and not f.endswith('__init__.py')]
    to_load = all_modules
    return to_load
    return all_modules
def get_all_plugins() -> List[str]:
    """ list all plugins """
    plugins = get_import_path(ROOT, "/" if len(sys.argv) == 2 and sys.argv[1] == 'dev' else "/**/")
    _LOG.debug("All Available Plugins: %s", plugins)
    return list(plugins)

__all__ = ['ROOT', 'get_all_plugins']
ALL_INB= sorted(__list_all_modules())
#log.info("Userbot module loaded: %s", str(ALL_OWN))
__all__ = ALL_INB + ["ALL_INB"]
