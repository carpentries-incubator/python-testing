---
layout: page
title: Testing
subtitle: Fixtures
minutes: 10
---
> ## Learning Objectives {.objectives}
>
> -   Understand how test fixtures can help write tests.

The above example didn't require much setup or teardown. Consider, however, the
following example that could arise when comunicating with third-party programs.
You have a function `f()` which will write a file named `yes.txt` to disk with
the value 42 but only if a file `no.txt` does not exist. To truly test the
function works, you would want to ensure that neither `yes.txt` nor `no.txt`
existed before you ran your test. After the test, you want to clean up after
yourself before the next test comes along.  You could write the test, setup,
and teardown functions as follows:

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
    assert obs == exp
    # The last action of test_f() is to clean up after itself.
    f_teardown()
~~~

The above implementation of setup and teardown is usually fine.
However, it does
not guarantee that the
`f_setup()` and the `f_teardown()` functions will be called. This is becaue an
unexpected error anywhere in the body of `f()` or `test_f()` will cause the
test to abort before the teardown function is reached.

These setup and teardown behaviors are needed when _test fixtures_ must be
created.  A fixture is any environmental state or object that is required for the test to successfully run.

As above, a function that is executed before the test to prepare the fixture
is called a _setup_ function. One that is executed to mop-up side effects
after a test is run is called a _teardown_ function.
By giving our setup and teardown functions special names pytest will
ensure that they are run before and after our test function regardless of
what happens in the test function.
Those special names are `setup_function` and `teardown_function`,
and each needs to take a single argument: the test function being run
(in this case we will not use the argument).


~~~ {.python}
import os

from mod import f

def setup_function(func):
    # The setup_function() function tests ensure that neither the yes.txt nor the
    # no.txt files exist.
    files = os.listdir('.')
    if 'no.txt' in files:
        os.remove('no.txt')
    if 'yes.txt' in files:
        os.remove('yes.txt')

def teardown_function(func):
    # The f_teardown() function removes the yes.txt file, if it was created.
    files = os.listdir('.')
    if 'yes.txt' in files:
        os.remove('yes.txt')

def test_f():
    exp = 42
    f()
    with open('yes.txt', 'r') as fhandle:
        obs = int(fhandle.read())
    assert obs == exp
~~~

The setup and teardown functions make our test simpler and the teardown
function is guaranteed to be run even if an exception happens in our test.
In addition, the setup and teardown functions will be automatically called for
_every_ test in a given file so that each begins and ends with clean state.
(Pytest has its own neat [fixture system](http://pytest.org/latest/fixture.html#fixture)
that we won't cover here.)


## Unittest

The `unittest` module also provides this functionality for us with the `setUp` and `tearDown` methods that allow you to define instructions that will be executed before and after each test method (note the capitalisation of these names, which is important).

~~~ {.python}
import os
import unittest

def f():
    files = os.listdir('.')
    if 'no.txt' not in files:
        with open('yes.txt', 'w') as yesfile:
            yesfile.write('42')

class TestMod(unittest.TestCase):
    def setUp(self):
        # The setUp() function tests ensure that neither the yes.txt nor the
        # no.txt files exist.
	# unittest will run this before each test case is run.
        files = os.listdir('.')
        if 'no.txt' in files:
            os.remove('no.txt')
        if 'yes.txt' in files:
            os.remove('yes.txt')

    def tearDown(self):
        # The tearDown() function removes the yes.txt file, if it was created.
	# unittest will run this after each test case
        files = os.listdir('.')
        if 'yes.txt' in files:
            os.remove('yes.txt')

    def test_f(self):
        # The first action of test_f() is to make sure the file system is clean.
        exp = 42
        f()
        with open('yes.txt', 'r') as fhandle:
            obs = int(fhandle.read())
        self.assertEqual(obs, exp)

if __name__ == '__main__':
    unittest.main()
~~~

~~~ {.bash}
python test_setup_teardown.py
~~~

~~~ {.output}
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

~~~
