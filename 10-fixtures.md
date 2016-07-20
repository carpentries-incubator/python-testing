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

    assert exp == obd
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
after a test is run is called a _tear-down_ function.


To make sure that both setup and tear-down are executed, we can use a `py.test`'s `yield_fixture`.
This decorator can be used to combine setup and tear-down logic into a single, self-contained _fixture_ function.
The name of the fixture function can then be provided as an argument to any tests which use the same fixture.


~~~ {.python}

from pytest import yield_fixture

@yield_fixture
def f_fixture():
    # The setup code runs before the test
    f_setup()

    # This will transfer control to the test
    yield

    # Everything after the yield runs after the test
    f_teardown()


def test_f(f_fixture):
    exp = 42
    f()
    with open('yes.txt', 'r') as fhandle:
        obs = int(fhandle.read())
    assert exp == obd
~~~

In the above example, `f_setup` is always called before `test_f` executes, and `f_teardown` is called afterwards,
even if `test_f` fails unexpectedly.  Note that there is generally no need to keep `f_setup` and `f_teardown` as
separate functions: any code above the `yield` will be interpreted as setup, and any code afterward is considered
tear-down.
