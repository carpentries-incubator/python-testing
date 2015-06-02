---
layout: page
title: Testing
subtitle: Assertions
minutes: 10
---
> ## Learning Objectives {.objectives}
> 
> *   Assertions are one line tests embedded in code.
> *   Assertions can halt execution if something unexpected happens.
> *   Assertions are the building block of tests.


Assertions are the simplest type of test. They are used as a tool for bounding 
acceptable behavior during runtime. The assert keyword in python has the 
following behavior:

~~~ {.python}
>>> assert True == False
~~~
~~~ {.output}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  AssertionError
~~~
~~~ {.python}
  >>> assert True == True
~~~
~~~ {.output}
  >>>
~~~

That is, assertions halt code execution instantly if the comparison is false. 
It does nothing at all if the comparison is true. These are therefore a very 
good tool for guarding the function against foolish (e.g. human) input:

~~~ {.python}
def mean(num_list):
    assert len(num_list) != 0
    return sum(num_list)/len(num_list)
~~~

The advantage of assertions is their ease of use. They are rarely more than one
line of code. The disadvantage is that assertions halt execution
indiscriminately and the helpfulness of the resulting error message is usually
quite limited. 


> ## Insert an Assertion {.challenge}
>
> In the following code, insert an assertion that checks whether the list is 
> made of numbers.
> 
> ~~~ {.python}
> def mean(num_list):
>   return sum(num_list)/len(num_list)
> ~~~


Assertions are also helpful for catching abnormal behaviors, such as those that 
arise with floating point arithmetic.

> ## Check a Floating Point Error {.challenge}
> a = 401.0/200.0
> 
> 1. Using the `assert` keyword, how could you test whether `a` is the same as 
> int (a) to within 2 decimal places?
> 
> 2. How about within an error of 0.003?

To help with situations such as those above, there are classes of more helpful 
assertions that we will use often in later parts of this testing lesson as the 
building blocks of our tests. The nose testing package contains many of them.


~~~ {.python}
from nose.tools import assert_almost_equal
> a = 401./200.
> assert_almost_equal(a, int(a), places=2)
> assert_almost_equal(a, int(a), delta=0.003)
~~~

These assertions give much more helpful error messages and have much more 
powerful features than the simple assert keyword. An even more powerful sibling 
of the assertion is the _exception_. We'll learn about those in the next 
lesson.
