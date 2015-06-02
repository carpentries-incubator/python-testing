---
layout: page
title: Testing
subtitle: Unit Tests
minutes: 10
---
> ## Learning Objectives {.objectives}
> 
> *   Understand that functions are the atomistic unit of software.
> *   Understand that simpler units are easier to test than complex ones.
> *   Understand how to write a single unit test.
> *   Understand how to run a single unit test.
> *   Understand how test fixtures can help write tests.

Unit tests are so called because they exercise the functionality of the code by
interrogating individual functions and methods. Fuctions and methods can often
be considered the atomic units of software because they are indivisble.
However, what is considered to be the smallest code _unit_ is subjective. The
body of a function can be long are short, and shorter functions are arguably
more unit-like than long ones.

Thus what reasonably constitutes a code unit typically varies from project to
project and language to language.  A good guideline is that if the code cannot
be made any simpler logically (you cannot split apart the addition operator) or
practically (a function is self-contained and well defined), then it is a unit. 

> ## Functions are Like Paragraphs {.callout}
> Recall that humans can only hold a few ideas in our heads at once. Paragraphs
> in books, for example, become unwieldy after a few lines. Functions, generaly,
> shouldn't be longer than paragraphs.
> Robert C. Martin, the author of "Clean Code" said : "The first rule of
> functions is that _they should be small_. The second rule of functions is that
> _they should be smaller than that_." 

The desire to unit test code often has the effect of encouraging both the
code and the tests to be as small, well-defined, and modular as possible.  
In Python, unit tests typically take the form of test functions that call and make
assertions about methods and functions in the code base.  To run these test
functions, a test framework is often required to collect them together. For
now, we'll write some tests for the mean function and simply run them
individually to see whether they fail. In the next session, we'll use a test
framework to collect and run them.

Unit tests are typically made of three pieces, some set-up, a number of
assertions, and some tear-down. Set-up can be as simple as initializing the
input values or as complex as creating and initializing concrete instances of a
class. Ultimately, the test occurs when an assertion is made, comparing the
observed and expected values.

> ## Write a File Full of Tests {.challenge}
> 1. In a file called `test_mean.py`, implement the following code:
> 
> ~~~ {.python}
> from mean import *
> 
> def test_ints():
>   num_list=[1,2,3,4,5]
>   obs = mean(num_list)
>   exp = 3
>   assert obs == exp
> 
> def test_zero():
>   num_list=[0,2,4,6]
>   obs = mean(num_list)
>   exp = 3
>   assert obs == exp
> 
> def test_double():
>   num_list=[1,2,3,4]
>   obs = mean(num_list)
>   exp = 2.5
>   assert obs == exp
> 
> def test_long():
>   big = 100000000
>   obs = mean(range(1,big))
>   exp = big/2.0
>   assert obs == exp
> ~~~
> 
> 2. Use IPython to import the test_mean package and run each test.
> 


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
after a test is run is called a _teardown_ function.  Nose has a decorator that
you can use to automatically run setup and teardown of fixtures no matter if 
the test succeeded, failed, or had an error.

To make sure that both of the functions will be executed, you must use nose's
`with_setup()` decorator. This decorator may be applied to any test
and takes a setup and a teardown function as possible arguments. We can rewrite the
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
