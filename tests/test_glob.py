from glob import glob


TEST_DIR = '/Users/liuyuan/projects/streamparse/streamparse/'

# glob用于查找匹配某个路径下的文件
files = glob(TEST_DIR + '*.py')
print(files)

"""
['/Users/liuyuan/projects/streamparse/streamparse/run.py', '/Users/liuyuan/projects/streamparse/streamparse/version.py', '/Users/liuyuan/projects/streamparse/streamparse/util.py', '/Users/liuyuan/projects/streamparse/streamparse/bolt.py', '/Users/liuyuan/projects/streamparse/streamparse/__init__.py', '/Users/liuyuan/projects/streamparse/streamparse/thrift.py', '/Users/liuyuan/projects/streamparse/streamparse/spout.py', '/Users/liuyuan/projects/streamparse/streamparse/component.py']
"""

# 匹配所有文件, 目录, 只匹配第一层, recursive=True会递归输出所有子目录
files2 = glob(TEST_DIR + '**')
print(files2)