---
title: Unit Tests
teaching: 10
exercises: 0
questions:
- "What is a unit of code?"
objectives:
- "Understand that functions are the atomistic unit of software."
- "Understand that simpler units are easier to test than complex ones."
- "Understand how to write a single unit test."
- "Understand how to run a single unit test."
- "Understand how test fixtures can help write tests."
keypoints:
- "Functions are the atomistic unit of software."
- "Simpler units are easier to test than complex ones."
- "A single unit test is a function containing assertions."
- "Such a unit test is run just like any other function."
- "Running tests one at a time is pretty tedious, so we will use a framework instead."
---

Unit tests are so called because they exercise the functionality of the code by
interrogating individual functions and methods. Functions and methods can often
be considered the atomic units of software because they are indivisible.
However, what is considered to be the smallest code _unit_ is subjective. The
body of a function can be long are short, and shorter functions are arguably
more unit-like than long ones.

Thus what reasonably constitutes a code unit typically varies from project to
project and language to language.  A good guideline is that if the code cannot
be made any simpler logically (you cannot split apart the addition operator) or
practically (a function is self-contained and well defined), then it is a unit. 

> ## Functions are Like Paragraphs
>
> Recall that humans can only hold a few ideas in our heads at once. Paragraphs
> in books, for example, become unwieldy after a few lines. Functions, generally,
> shouldn't be longer than paragraphs.
> Robert C. Martin, the author of "Clean Code" said : "The first rule of
> functions is that _they should be small_. The second rule of functions is that
> _they should be smaller than that_." 
{: .callout}

The desire to unit test code often has the effect of encouraging both the
code and the tests to be as small, well-defined, and modular as possible.  
In Python, unit tests typically take the form of test functions that call and make
assertions about methods and functions in the code base.  To run these test
functions, a test framework is often required to collect them together. For
now, we'll write some tests for the mean function and simply run them
individually to see whether they fail. In the next session, we'll use a test
framework to collect and run them.

## Unit Tests Are Just Functions

Unit tests are typically made of three pieces, some set-up, a number of
assertions, and some tear-down. Set-up can be as simple as initializing the
input values or as complex as creating and initializing concrete instances of a
class. Ultimately, the test occurs when an assertion is made, comparing the
observed and expected values. For example, let us test that our mean function 
successfully calculates the known value for a simple list.

~~~
from mean import *

def test_ints():
    num_list = [1, 2, 3, 4, 5]
    obs = mean(num_list)
    exp = 3
    assert obs == exp
~~~
{: .python}

The test above: 
- sets up the input parameters (the simple list [1, 2, 3, 4, 5].
- collects the observed result
- declares the expected result (calculated with our human brain).
- and compares the two with an assertion.

A unit test suite is made up of many tests just like this one. A single
implemented function may be tested in numerous ways.

In a file called `test_mean.py`, implement the following code:

~~~
from mean import *

def test_ints():
    num_list = [1, 2, 3, 4, 5]
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

Use IPython to import the `test_mean` package and run each test.

Well, **that** was tedious.