---
title: Assertions
teaching: 10
exercises: 0
questions:
- "How can we compare observed and expected values?"
objectives:
- "Assertions are one line tests embedded in code."
- "Assertions can halt execution if something unexpected happens."
- "Assertions are the building blocks of tests."
keypoints:
- "Assertions are one line tests embedded in code."
- "The `assert` keyword is used to set an assertion."
- "Assertions halt execution if the argument is false."
- "Assertions do nothing if the argument is true."
- "The `numpy.testing` module provides tools numeric testing."
- "Assertions are the building blocks of tests."
---

Assertions are the simplest type of test. They are used as a tool for bounding
acceptable behavior during runtime. The assert keyword in python has the
following behavior:

~~~
>>> assert True == False
~~~
{: .python}
~~~
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  AssertionError
~~~
{: .output}
~~~
>>> assert True == True
~~~
{: .python}
~~~
~~~
{: .output}

That is, assertions halt code execution instantly if the comparison is false.
It does nothing at all if the comparison is true. These are therefore a very
good tool for guarding the function against foolish (e.g. human) input:

~~~
def mean(num_list):
    assert len(num_list) != 0
    return sum(num_list)/len(num_list)
~~~
{: .python}

The advantage of assertions is their ease of use. They are rarely more than one
line of code. The disadvantage is that assertions halt execution
indiscriminately and the helpfulness of the resulting error message is usually
quite limited.

Also, input checking may require decending a rabbit hole of exceptional cases.
What happens when the input provided to the mean function is a string, rather
than a list of numbers?

1. Open a [Jupyter Notebook](https://jupyter.org/)
2. Create the following function:

~~~
def mean(num_list):
  return sum(num_list)/len(num_list)
~~~
{: .python}

3. In the function, insert an assertion that checks whether the input is actually a list.

> ## Hint
>
> Hint: Use the [isinstance function](https://docs.python.org/2/library/functions.html#isinstance).
{: .callout}

> ## Testing Near Equality
>
> Assertions are also helpful for catching abnormal behaviors, such as those
> that arise with floating point arithmetic. Using the assert keyword, how could
> you test whether some value is almost the same as another value?
>
> - A program provides the number `a`.
> - Use the `assert` keyword to check whether the number `a` is greater than 2.
> - Use the `assert` keyword to check that `a` is equal to 2 within an error of 0.003.
{: .callout}

~~~
a = 2.002
# greater than 2 assertion here
# 0.003 assertion here
~~~
{: .python}

We can think of assertions as fences set up to keep undesirable output out of our function.  Fences are barriers employed to block program execution if the state isn't adequate to the intended task.  Assertion fences are crude but effective ways to check input.

>Consider the following function.
>
>If one were to include a fence as the first line of this function, what would be an appropriate fence to avoid a ZeroDivisionError?
{: .callout}

~~~
def mean( num_list ):
    return sum( num_list ) / len( num_list )
~~~
{: .python}

## NumPy

The NumPy numerical computing library has a built-in function `assert_allclose`
for comparing numbers within a tolerance:

~~~
from numpy.testing import assert_allclose
from mynum import a
assert_allclose(a, 2, atol=0.003, rtol=0)
~~~
{: .python}
