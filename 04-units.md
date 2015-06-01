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
> Robert C. Martin, the author of "Clean Code" said : TODO

The desire to unit test code often has the effect of encouraging both the
code and the tests to be as small, well-defined, and modular as possible.  
In Python, unit tests typically take the form of test functions.

Consider the following example that could arise when comunicating with
third-party programs. You have a function `f()` which will write a file
named `yes.txt`
to disk with the value 42 but only if a file `no.txt` does not exist. To truly
test the function works, you would want to ensure that neither `yes.txt` nor
`no.txt` existed before you ran your test. After the test, you want to clean
up after yourself before the next test comes along.  You could write the
test, setup, and teardown functions as follows:

[source,python]
---------------
import os

from nose.tools import assert_equal, with_setup

from mod import f

def f_setup(): <1>
    files = os.listdir('.')
    if 'no.txt' in files:
        os.remove('no.txt')
    if 'yes.txt' in files:
        os.remove('yes.txt')

def f_teardown(): <2>
    files = os.listdir('.')
    if 'yes.txt' in files:
        os.remove('yes.txt')

def test_f():
    f_setup() <3>
    exp = 42
    f()
    with open('yes.txt', 'r') as fhandle:
        obs = int(fhandle.read())
    assert_equal(exp, obd)
    f_teardown() <4>
---------------
<1> The +f_setup()+ function tests ensure that neither the +yes.txt+ nor
    the +no.txt+ files exist.
<2> The +f_teardown()+ function removes the +yes.txt+ file, if it was created.
<3> The first action of +test_f()+ is to make sure the file system is clean.
<4> The last action of +test_f()+ is to clean up after itself.

The above implementation of test fixtures is usually fine.  However, it does
not guarantee that the
+f_setup()+ and the +f_teardown()+ functions will be called. This is becaue an
unexpected error anywhere in the body of +f()+ or +test_f()+ will cause the
test to abort before the teardown function is reached.
To make sure that both of the fixtures will be executed, you must use nose's
+with_setup()+ decorator. This decorator may be applied to any test
and takes a setup and a teardown function as possible arguments. We can rewrite the
+test_f()+ to be wrapped by +with_setup()+.


[source,python]
---------------
@with_setup(setup=f_setup, teardown=f_teardown)
def test_f():
    exp = 42
    f()
    with open('yes.txt', 'r') as fhandle:
        obs = int(fhandle.read())
    assert_equal(exp, obd)
---------------

Note that if you have functions in your test module that are simply named
+setup()+ and +teardown()+, each of these are called automatically when the
entire test module is loaded in and finished.

.Write Simple Functions
[TIP]
====
Simple tests are the easiest to write. For this reason, functions should be
small enough that they are easy to test. For more information on writing
code that facilitates tests, we recommend the Robert C. Martin book, 'Clean
Code.'
====

Having introduced the concept of unit tests, we can now go up a level in
complexity.


*Aside on Fixtures*

Additionally, unit tests may have
_test fixtures_.  A fixture is anything that may be added to the test
that creates or removes the environment required by the test to
successfully run.  They are not
part of expected result, the observed result, or the assertion.  Test
fixtures are completely optional.

A fixture that is executed before the test to prepare the environment
is called a _setup_ function. One that is executed to mop-up side effects
after a test is run is called a _teardown_ function.  Nose has a decorator that
you can use to automatically run fixtures no matter if the test succeeded,
failed, or had an error.


> ## Places to Create Git Repositories {.challenge}
>
> Dracula starts a new project, `moons`, related to his `planets` project.
> Despite Wolfman's concerns, he enters the following sequence of commands to
> create one Git repository inside another:
> 
> ~~~ {.bash}
> cd             # return to home directory
> mkdir planets  # make a new directory planets
> cd planets     # go into planets
> git init       # make the planets directory a Git repository
> mkdir moons    # make a sub-directory planets/moons
> cd moons       # go into planets/moons
> git init       # make the moons sub-directory a Git repository
> ~~~
> 
> Why is it a bad idea to do this?
> How can Dracula "undo" his last `git init`?
