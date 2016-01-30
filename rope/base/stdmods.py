import re
import os
import sys

from rope.base import utils
from rope import comp


def _stdlib_path():
    if comp.PY2:
        from distutils import sysconfig
        return sysconfig.get_python_lib(standard_lib=True,
                                        plat_specific=True)
    elif comp.PY3:
        # @todo, it works with this stuff.. maybe it would work well
        # on travis, not sure yet
        # return '/home/sergeyg/.virtualenvs/rit/lib/python3.4'
        import sysconfig
        return sysconfig.get_config_var('LIBDIR')


@utils.cached(1)
def standard_modules():
    return python_modules() | dynload_modules()


@utils.cached(1)
def python_modules():
    result = set()
    lib_path = _stdlib_path()
    if os.path.exists(lib_path):
        for name in os.listdir(lib_path):
            path = os.path.join(lib_path, name)
            if os.path.isdir(path):
                if '-' not in name:
                    result.add(name)
            else:
                if name.endswith('.py'):
                    result.add(name[:-3])
    return result


def normalize_so_name(name):
    """
    Handle different types of python installations
    """
    return re.sub('\.cpython-\d+', '', os.path.splitext(name)[0].replace('module', ''))


@utils.cached(1)
def dynload_modules():
    result = set(sys.builtin_module_names)
    dynload_path = os.path.join(_stdlib_path(), 'lib-dynload')
    if os.path.exists(dynload_path):
        for name in os.listdir(dynload_path):
            path = os.path.join(dynload_path, name)
            if os.path.isfile(path):
                if name.endswith('.dll'):
                    result.add(os.path.splitext(name)[0])
                if name.endswith('.so'):
                    result.add(normalize_so_name(name))
    return result
