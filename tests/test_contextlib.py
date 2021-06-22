from contextlib import contextmanager


@contextmanager
def tag(name):
    try:
        print("start...")

        yield name

        print("end...")
    finally:
        print('finished..')


with tag("aaa") as n:
    print("hello world")
    raise Exception('something wrong')
    print(n)


"""
start...
hello world
finished..
Traceback (most recent call last):
  File "/Users/liuyuan/projects/apache-storm/tests/test_contextlib.py", line 18, in <module>
    raise Exception('something wrong')
Exception: something wrong
"""