---
layout: page
title: Testing
subtitle: Running Tests with Nose
minutes: 10
---
> ## Learning Objectives {.objectives}
> 
> -   Understand how to run a test suite using the nose framework
> -   Understand how to read the output of a nose test suite


Recall that we created a suite of tests for our mean function.

~~~ {.python}
from mean import *

def test_ints():
  num_list=[1,2,3,4,5]
  obs = mean(num_list)
  exp = 3
  assert obs == exp

def test_zero():
  num_list=[0,2,4,6]
  obs = mean(num_list)
  exp = 3
  assert obs == exp

def test_double():
  num_list=[1,2,3,4]
  obs = mean(num_list)
  exp = 2.5
  assert obs == exp

def test_long():
  big = 100000000
  obs = mean(range(1,big))
  exp = big/2.0
  assert obs == exp
~~~

Once these tests are written in a file called `test_mean.py`, the command
"nosetests" can be called from the directory containing the tests:

~~~ {.bash}
$ nosetests
~~~
~~~ {.output}
..F.
FAIL: test_mean.test_double
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/khuff/anaconda/lib/python2.7/site-packages/nose/case.py", line 197, in runTest
    self.test(*self.arg)
  File "/Users/khuff/repos/book-code/tests/test_mean.py", line 20, in test_double
    assert obs == exp
AssertionError

----------------------------------------------------------------------
Ran 4 tests in 3.062s

FAILED (failures=1)
~~~

In the above case, the python nose package 'sniffed-out' the tests in the
directory and ran them together to produce a report of the sum of the files and
functions matching the regular expression `[Tt]est[-_]*`.


The major boon a testing framework provides is exactly that, a utility to find and run the
tests automatically. With `nose`, this is the command-line tool called
_nosetests_.  When _nosetests_ is run, it will search all the directories whose names start or
end with the word _test_, find all of the Python modules in these directories
whose names
start or end with _test_, import them, and run all of the functions and classes
whose names start or end with _test_. In fact, `nose` looks for any names
that match the regular expression `'(?:^|[\\b_\\.-])[Tt]est'`.
This automatic registration of test code saves tons of human time and allows us to
focus on what is important: writing more tests.

When you run _nosetests_, it will print a dot (`.`) on the screen for every test
that passes,
an `F` for every test that fails, and an `E` for every test were there was an
unexpected error. In rarer situations you may also see an `S` indicating a
skipped tests (because the test is not applicable on your system) or a `K` for a known
failure (because the developers could not fix it promptly). After the dots, _nosetests_
will print summary information. 


> ## Fix The Failing Code {.challenge}
> Without changing the tests, alter the mean.py file from the previous section until it passes. 
> When it passes, _nosetests_ will produce results like the following:
>
> ~~~ {.bash}
> $ nosetests
> ~~~
> ~~~ {.output}
> ....
> 
> Ran 4 test in 0.4s
>
> OK
> ~~~

As we write more code, we would write more tests, and _nosetests_ would produce
more dots.  Each passing test is a small, satisfying reward for having written
quality scientific software. Now that you know how to write tests, let's go
into what can go wrong.


> ## Key Points {.keypoints}
>
> -   The `nosetests` command collects and runs tests starting with `Test-`, `test_`, and similar names.
> -   `.` means the test passed
> -   `F` means the test failed
> -   `E` encountered an error
> -   `K` is a known failure
> -   `S` is a purposefully skipped test
