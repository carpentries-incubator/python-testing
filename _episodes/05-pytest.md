---
title: Running Tests with pytest
teaching: 10
exercises: 0
questions:
- "FIXME"
objectives:
- "Understand how to run a test suite using the pytest framework"
- "Understand how to read the output of a pytest test suite"
keypoints:
- "The `py.test` command collects and runs tests starting with `Test` or `test_`."
- "`.` means the test passed"
- "`F` means the test failed or erred"
- "`x` is a known failure"
- "`s` is a purposefully skipped test"
---

We created a suite of tests for our mean function, but it was annoying to run
them one at a time. It would be a lot better if there were some way to run them
all at once, just reporting which tests fail and which succeed.

Thankfully, that exists. Recall our tests:

~~~
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
{: .python}

Once these tests are written in a file called `test_mean.py`, the command
`py.test` can be called from the directory containing the tests:

~~~
$ py.test
~~~
{: .bash}
~~~
collected 5 items

test_mean.py ....F

================================== FAILURES ===================================
________________________________ test_complex _________________________________

    def test_complex():
        # given that complex numbers are an unordered field
        # the arithmetic mean of complex numbers is meaningless
        num_list = [2 + 3j, 3 + 4j, -32 - 2j]
        obs = mean(num_list)
        exp = NotImplemented
>       assert obs == exp
E       assert (-9+1.6666666666666667j) == NotImplemented

test_mean.py:34: AssertionError
===================== 1 failed, 4 passed in 2.71 seconds ======================
~~~
{: .output}

In the above case, the pytest package 'sniffed-out' the tests in the
directory and ran them together to produce a report of the sum of the files and
functions matching the regular expression `[Tt]est[-_]*`.

The major boon a testing framework provides is exactly that, a utility to find and run the
tests automatically. With pytest, this is the command-line tool called
`py.test`.  When `py.test` is run, it will search all directories below where it was called,
find all of the Python files in these directories whose names
start or end with `test`, import them, and run all of the functions and classes
whose names start with `test` or `Test`.
This automatic registration of test code saves tons of human time and allows us to
focus on what is important: writing more tests.

When you run `py.test`, it will print a dot (`.`) on the screen for every test
that passes,
an `F` for every test that fails or where there was an unexpected error.
In rarer situations you may also see an `s` indicating a
skipped tests (because the test is not applicable on your system) or a `x` for a known
failure (because the developers could not fix it promptly). After the dots, pytest
will print summary information.

> Without changing the tests, alter the mean.py file from the previous section until it passes.
> When it passes, `py.test` will produce results like the following:
>
> ~~~
> $ py.test
> ~~~
> {: .bash}
> ~~~
> collected 5 items
>
> test_mean.py .....
>
> ========================== 5 passed in 2.68 seconds ===========================
> ~~~
> {: .output}

As we write more code, we would write more tests, and pytest would produce
more dots.  Each passing test is a small, satisfying reward for having written
quality scientific software. Now that you know how to write tests, let's go
into what can go wrong.
