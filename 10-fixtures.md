---
layout: page
title: Testing
subtitle: Fixtures
minutes: 10
---
> ## Learning Objectives {.objectives}
>
> -   Understand how test fixtures can help write tests.

The above example didn't require much setup or tear-down. Consider, however, the
following example that could arise when communicating with third-party programs.
You have a function `f()` which will write a file named `yes.txt` to disk with
the value 42 but only if a file `no.txt` does not exist. To truly test the
function works, you would want to ensure that neither `yes.txt` nor `no.txt`
existed before you ran your test. After the test, you want to clean up after
yourself before the next test comes along.  You could write the test, setup,
and tear-down functions as follows:

~~~ {.python}
import os

from nose.tools import assert_equal, with_setup

from mod import f

def f_setup():
    # The f_setup() function tests ensure that neither the yes.txt nor the
    # no.txt files exist.
    files = os.listdir('.')
    if 'no.txt' in files:
        os.remove('no.txt')
    if 'yes.txt' in files:
        os.remove('yes.txt')

def f_teardown():
    # The f_teardown() function removes the yes.txt file, if it was created.
    files = os.listdir('.')
    if 'yes.txt' in files:
        os.remove('yes.txt')

def test_f():
    # The first action of test_f() is to make sure the file system is clean.
    f_setup()
    exp = 42
    f()
    with open('yes.txt', 'r') as fhandle:
        obs = int(fhandle.read())
    assert_equal(exp, obd)
    # The last action of test_f() is to clean up after itself.
    f_teardown()
~~~

The above implementation of setup and tear-down is usually fine.
However, it does
not guarantee that the
`f_setup()` and the `f_teardown()` functions will be called. This is because an
unexpected error anywhere in the body of `f()` or `test_f()` will cause the
test to abort before the tear-down function is reached.

These setup and tear-down behaviors are needed when _test fixtures_ must be
created.  A fixture is any environmental state or object that is required for the test to successfully run.

As above, a function that is executed before the test to prepare the fixture
is called a _setup_ function. One that is executed to mop-up side effects
after a test is run is called a _tear-down_ function.  Nose has a decorator that
you can use to automatically run setup and tear-down of fixtures no matter if
the test succeeded, failed, or had an error.

To make sure that both of the functions will be executed, you must use nose's
`with_setup()` decorator. This decorator may be applied to any test
and takes a setup and a tear-down function as possible arguments. We can rewrite the
`test_f()` to be wrapped by `with_setup()`.


~~~ {.python}
@with_setup(setup=f_setup, teardown=f_teardown)
def test_f():
    exp = 42
    f()
    with open('yes.txt', 'r') as fhandle:
        obs = int(fhandle.read())
    assert_equal(exp, obd)
~~~

Note that if you have functions in your test module that are simply named
`setup()` and `teardown()`, each of these are called automatically when the
entire test module is loaded in and finished.
