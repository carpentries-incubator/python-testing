---
layout: page
title: Testing
subtitle: Edge and Corner Cases
minutes: 10
---
> ## Learning Objectives {.objectives}
>
> -   Understand that edge  cases are at the limit of the function's behavior
> -   Write a test for an edge case
> -   Understand that corner cases are where two edge cases meet
> -   Write a test for a corner case

What we saw in the tests for the mean function are called  _interior_ tests.
The precise points that we tested did not matter. The mean function should have
behaved as expected when it is within the valid range.


## Edge Cases

The situation where the test examines either the beginning or the end of a range, but
not the middle, is called an _edge case_. In a simple, one-dimensional
problem, the two edge cases should always be tested along with at least
one internal point. This ensures that you have good _coverage_ over the
range of values.

Anecdotally, it is important to test edges cases because this is where errors tend to
arise. Qualitatively different behavior happens at boundaries. As such,
they tend to have special code dedicated to them in the implementation.

> ## Consider the Fibonacci Sequence {.callout}
>
> Take a moment to recall everything you know about the Fibonacci sequence.
>
> The fibonacci sequence is valid for all positive integers. To believe that a
> fibonacci sequence function is accurate throughout that space, is it necessary
> to check every expected output value of the fibonacci sequence? Given that the
> sequence is infinite, let's hope not.
>
> Indeed, what we should probably do is test a few values within the typical
> scope of the function, and then test values at the limit of the function's
> behavior.


Consider the following simple Fibonacci function:

~~~ {.python}
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
~~~

This function has two edge cases: zero and one. For these values of `n`, the
`fib()` function does something special that does not apply to any other values.
Such cases should be tested explicitly. A minimally sufficient test suite
for this function would be:

~~~ {.python}
from mod import fib

def test_fib0():
    # test edge 0
    obs = fib(0)
    assert obs == 1

def test_fib1():
    # test edge 1
    obs = fib(1)
    assert obs == 1

def test_fib6():
    # test internal point
    obs = fib(6)
    assert obs == 13)
~~~

Different functions will have different edge cases.
Often, you need not test for cases that are outside the valid range, unless you
want to test that the function fails.  In the `fib()` function negative and
noninteger values are not valid inputs. Tests for these classes of numbers serve you well if you want to make sure that the function fails as
expected. Indeed, we learned in the assertions section that this is actually quite a good idea.

> ## Test for Graceful Failure {.challenge}
>
> The `fib()` function should probably return the Python built-in
> `NotImplemented` value for negative and noninteger values.
>
> 1. Create a file called `test_fib.py`
> 2. Copy the three tests above into that file.
> 3. Write **two new** tests that check for the expected return value
> (NotImplemented) in each case (for negative input and noninteger input
> respectively).

Edge cases are not where the story ends, though, as we will see next.

## Corner Cases

When two or more edge cases are combined, it is called a _corner case_.
If a function is parametrized by two linear and independent variables, a test
that is at the extreme of both variables is in a corner. As a demonstration,
consider the case of the function `(sin(x) / x) * (sin(y) / y)`, presented here:

~~~ {.python}
import numpy as np

def sinc2d(x, y):
    if x == 0.0 and y == 0.0:
        return 1.0
    elif x == 0.0:
        return np.sin(y) / y
    elif y == 0.0:
        return np.sin(x) / x
    else:
        return (np.sin(x) / x) * (np.sin(y) / y)
~~~

The function `sin(x)/x` is called the `sinc()` function.  We know that at
the point where `x = 0`, then
`sinc(x) == 1.0`.  In the code just shown, `sinc2d()` is a two-dimensional version
of this function. When both `x` and `y`
are zero, it is a corner case because it requires a special value for both
variables. If either `x` or `y` but not both are zero, these are edge
cases. If neither is zero, this is a regular internal point.

A minimal test suite for this function would include a separate test for the
each of the edge cases, and an internal point. For example:

~~~ {.python}
import numpy as np

from mod import sinc2d

def test_internal():
    exp = (2.0 / np.pi) * (-2.0 / (3.0 * np.pi))
    obs = sinc2d(np.pi / 2.0, 3.0 * np.pi / 2.0)
    assert obs == exp

def test_edge_x():
    exp = (-2.0 / (3.0 * np.pi))
    obs = sinc2d(0.0, 3.0 * np.pi / 2.0)
    assert obs == exp

def test_edge_y():
    exp = (2.0 / np.pi)
    obs = sinc2d(np.pi / 2.0, 0.0)
    assert obs == exp
~~~

> ## Write a Corner Case {.challenge}
>
> The sinc2d example will also need a test for the corner case, where both x
> and y are 0.0.
>
> 1. Insert the sinc2d function code (above) into a file called mod.py.
> 2. Add the edge and internal case tests (above) to a test_sinc2d.py file.
> 3. Invent and implement a corner case test in that file.
> 4. Run all of the tests using `py.test` on the command line.

Corner cases can be even trickier to find and debug than edge cases because of their
increased complexity.  This complexity, however, makes them even more important to
explicitly test.

Whether internal, edge, or corner cases, we have started to build
up a classification system for the tests themselves. In the following sections,
we will build this system up even more based on the role that the tests have
in the software architecture.
