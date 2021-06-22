import pkgutil
import sys
import os
from os.path import dirname
import importlib


TEST_DIR = dirname(dirname(dirname(__file__))) + '/streamparse/streamparse'


def test1():
    for finder, mod_name, is_pkg in pkgutil.iter_modules([TEST_DIR]):
        print(finder, mod_name, is_pkg)
        print(finder.find_spec(mod_name))
        print()
        if not is_pkg and mod_name not in sys.modules:
            module = importlib.import_module(f"streamparse.{mod_name}") 

def test2():
    for root, dirnames, filenames in os.walk(TEST_DIR):
        print(root, dirnames, filenames)
        if root == TEST_DIR:
            for name in filenames:
                if name == '__init__.py':
                    continue
                mod_name = name.split('.')[0]
                module = importlib.import_module(f"streamparse.{mod_name}") 


test1()

"""
FileFinder('/Users/liuyuan/projects/streamparse/streamparse') spout False
ModuleSpec(name='spout', loader=<_frozen_importlib_external.SourceFileLoader object at 0x7fac26c39c90>, origin='/Users/liuyuan/projects/streamparse/streamparse/spout.py')

FileFinder('/Users/liuyuan/projects/streamparse/streamparse') storm True
ModuleSpec(name='storm', loader=<_frozen_importlib_external.SourceFileLoader object at 0x7fac26bd8490>, origin='/Users/liuyuan/projects/streamparse/streamparse/storm/__init__.py', submodule_search_locations=['/Users/liuyuan/projects/streamparse/streamparse/storm'])

FileFinder('/Users/liuyuan/projects/streamparse/streamparse') thrift False
ModuleSpec(name='thrift', loader=<_frozen_importlib_external.SourceFileLoader object at 0x7fac26bd8490>, origin='/Users/liuyuan/projects/streamparse/streamparse/thrift.py')
"""


test2()


"""
/Users/liuyuan/projects/streamparse/streamparse ['bootstrap', 'cli', 'storm', 'dsl'] ['run.py', 'version.py', 'util.py', 'bolt.py', '__init__.py', 'thrift.py', 'spout.py', 'component.py']
/Users/liuyuan/projects/streamparse/streamparse/bootstrap ['project'] ['__init__.py']
/Users/liuyuan/projects/streamparse/streamparse/bootstrap/project ['virtualenvs', 'topologies', 'src'] ['project.jinja2.clj', 'config.jinja2.json', 'gitignore', 'fabfile.py']
"""