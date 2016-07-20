---
layout: page
title: Testing
subtitle: Running Tests with py.test
minutes: 10
---
> ## Learning Objectives {.objectives}
> 
> -   Understand how to run a test suite using the py.test framework
> -   Understand how to read the output of a py.test test suite


We created a suite of tests for our mean function, but it was annoying to run 
them one at a time. It would be a lot better if there were some way to run them
all at once, just reporting which tests fail and which succeed.

Thankfully, that exists. Recall our tests:

~~~ {.python}
from mean import *

def test_ints():
    num_list = [1,2,3,4,5]
    obs = mean(num_list)
    exp = 3
    assert obs == exp

def test_zero():
    num_list=[0,2,4,6]
    obs = mean(num_list)
    exp = 3
    assert obs == exp

def test_double():
    # This one will fail in Python 2
    num_list=[1,2,3,4]
    obs = mean(num_list)
    exp = 2.5
    assert obs == exp

def test_long():
    big = 100000000
    obs = mean(range(1,big))
    exp = big/2.0
    assert obs == exp

def test_complex():
    # given that complex numbers are an unordered field
    # the arithmetic mean of complex numbers is meaningless
    num_list = [2 + 3j, 3 + 4j, -32 - 2j]
    obs = mean(num_list)
    exp = NotImplemented
    assert obs == exp
~~~

Once these tests are written in a file called `test_mean.py`, the command
"py.test" can be called from the directory containing the tests:

~~~ {.bash}
$ py.test test_mean.py
~~~
~~~ {.output}
============================== test session starts ===============================
platform linux -- Python 3.5.2, pytest-2.9.2, py-1.4.31, pluggy-0.3.1
rootdir: /home/bmcfee/git/swc/python-testing, inifile: 
plugins: pep8-1.0.6, cov-2.2.1
collected 5 items 

test_mean.py ....F

==================================== FAILURES ====================================
__________________________________ test_complex __________________________________

    def test_complex():
        # given that complex numbers are an unordered field
        # the arithmetic mean of complex numbers is meaningless
        num_list = [2 + 3j, 3 + 4j, -32 - 2j]
        obs = mean(num_list)
        exp = NotImplemented
>       assert obs == exp
E       assert (-9+1.6666666666666667j) == NotImplemented

test_mean.py:35: AssertionError
======================= 1 failed, 4 passed in 2.01 seconds =======================
~~~

In the above case, the _py.test_ package located the tests in the file `test_mean.py`
and ran them together to produce a report of the sum of the files and
functions matching the regular expression `[Tt]est[-_]*`.


The major boon a testing framework provides is exactly that, a utility to find and run the
tests automatically. With `py.test`, this is the command-line tool called
_py.test_.  When _py.test_ is run, it will search all the directories whose names start or
end with the word _test_, find all of the Python modules in these directories
whose names
start or end with _test_, import them, and run all of the functions and classes
whose names start or end with _test_. In fact, `py.test` looks for any names
that match the regular expression `'(?:^|[\\b_\\.-])[Tt]est'`.
This automatic registration of test code saves tons of human time and allows us to
focus on what is important: writing more tests.

When you run _py.test_, it will print a dot (`.`) on the screen for every test
that passes,
an `F` for every test that fails, and an `E` for every test were there was an
unexpected error. In rarer situations you may also see an `S` indicating a
skipped tests (because the test is not applicable on your system) or a `K` for a known
failure (because the developers could not fix it promptly). After the dots, _py.test_
will print summary information. 


> ## Fix The Failing Code {.challenge}
>
> Without changing the tests, alter the mean.py file from the previous section until it passes. 
> When it passes, _py.test_ will produce results like the following:
>
> ~~~ {.bash}
> $ py.test test_mean.py
> ~~~
> ~~~ {.output}
> ============================== test session starts ===============================
> platform linux -- Python 3.5.2, pytest-2.9.2, py-1.4.31, pluggy-0.3.1
> rootdir: /home/bmcfee/git/swc/python-testing, inifile: 
> plugins: pep8-1.0.6, cov-2.2.1
> collected 5 items 
> 
> test_mean_fixed.py .....
> 
> ============================ 5 passed in 2.00 seconds ============================
> ~~~

As we write more code, we would write more tests, and _py.test_ would produce
more dots.  Each passing test is a small, satisfying reward for having written
quality scientific software. Now that you know how to write tests, let's go
into what can go wrong.
