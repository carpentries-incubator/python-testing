---
layout: page
title: Testing
subtitle: The Unittest Module
minutes: 10
---
> ## Learning Objectives {.objectives}
>
> -   Understand how to use Unittest to write and run test cases
> -   Understand that Unittest can be used for many styles of test, not just unit tests
> -   
> -   

The Python standard library provides a module for writing and running tests, called `unittest`, which is documented for [Python3.6](https://docs.python.org/3.6/library/unittest.html?highlight=unittest#module-unittest) and [Python2.7](https://docs.python.org/2/library/unittest.html?highlight=unittest#module-unittest).

This module is useful for writing all styles of test, including unit tests and functional tests.

## Functional Tests

Functional testing is a way of checking software to ensure that it has all the required functionality that's specified within its functional requirements.  This will test many methods and may interact with dependencies like file access.

Functional tests are often the first tests that are written as part of writing a program.  They can link closely to a requirement: "This programme shall ...".

These tests are testing overall behaviour.

They are especially useful if code is being restructured or re-factored, to build confidence that the key behaviour is maintained during the restructuring.

Often true unit tests, as described in the previous page, test the implementation and may require changing at the same time as the code during a refactor.

## Unittest TestCases

unittest is part of the Python core library; it defines a class, unittest.TestCase which provides lots of useful machinery for writing tests.  We define classes which inherit from unittest.TestCase, bringing in their useful behaviour for us to apply to our tests.

The reuse of objects in this way is a really useful programming approach.  Don't worry if it is new to you.  For testing with unittest, you can just think of it as a framework to fit your test cases into.

We can rewrite the tests from the previous page, using the Unittest approach.

~~~ {.python}
import unittest

def mean(num_list):
    try:
        return sum(num_list)/len(num_list)
    except ZeroDivisionError :
        return 0
    except TypeError as detail :
        msg = ("The algebraic mean of an non-numerical list is undefined."
               " Please provide a list of numbers.")
        raise TypeError(detail.__str__() + "\n" +  msg)

class TestMean(unittest.TestCase):
    def test_ints(self):
        num_list = [1,2,3,4,5]
        obs = mean(num_list)
        exp = 3
        self.assertEqual(obs, exp)

    def test_zero(self):
        num_list=[0,2,4,6]
        obs = mean(num_list)
        exp = 3
        self.assertEqual(obs, exp)

    def test_double(self):
        # This one will fail in Python 2
        num_list=[1,2,3,4]
        obs = mean(num_list)
        exp = 2.5
        self.assertEqual(obs, exp)

    def test_long(self):
        big = 100000000
        obs = mean(range(1,big))
        exp = big/2.0
        self.assertEqual(obs, exp)

    def test_complex(self):
        num_list = [2 + 3j, 3 + 4j, -32 + 2j]
        obs = mean(num_list)
        exp = -9 + 3j
        self.assertEqual(obs, exp)

if __name__ == '__main__':
    unittest.main()
~~~

The naming of `class` and `def` entities is important.  All classes should be named beginning `Test` and all methods should be named beginning `test-`.  This enables the test runner to identify test cases to run.

Save this code to a file, e.g. `test_mean.py`, again beginning the name with `test_`.  This module can be run directly with python:

~~~ {.bash}
python test_mean.py
~~~

~~~ {.output}
.....
----------------------------------------------------------------------
Ran 5 tests in 2.053s

OK

~~~

Unittest reports failures and errors on test cases, which we can see if we run Python2, as one of our tests only passes in Python3:

~~~ {.bash}
python2 test_mean.py
~~~

~~~ {.output}
.F...
======================================================================
FAIL: test_double (__main__.TestMean)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_mean.py", line 31, in test_double
    self.assertEqual(obs, exp)
AssertionError: 2 != 2.5

----------------------------------------------------------------------
Ran 5 tests in 2.433s

FAILED (failures=1)
~~~
