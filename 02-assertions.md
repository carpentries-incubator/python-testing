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
> *   Assertions are the building blocks of tests.

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
> 1. Create a new IPython Notebook
> 2. Create the following function:
>
> ~~~ {.python}
> def mean(num_list):
>   return sum(num_list)/len(num_list)
> ~~~
>
> 3. In the function, insert an assertion that checks whether the list is 
> made of numbers.
> 


Assertions are also helpful for catching abnormal behaviors, such as those that 
arise with floating point arithmetic.

> ## Challenge: Almost Equal {.challenge}
> Assertions are also helpful for catching abnormal behaviors, such as those
> that arise with floating point arithmetic. Using the assert keyword, how could
> you test whether some value is almost the same as another value?
>
> - My package, mynum, provides the number a. 
> - Use the `assert` keyword to check whether the number a is greater than 2.
> - Use the `assert` keyword to check whether a is equal to 2 to within 2 decimal places.
> - Use the `assert` keyword to check that a is equal to 2 within an error of 0.003.
> 
> ~~~ {.python}
> from mynum import a
> # greater than 2 assertion here
> # 2 decimal places assertion here
> # 0.003 assertion here
> ~~~

To help with situations such as those above, there are classes of more helpful
assertions that we will use often in later parts of this testing lesson as the
building blocks of our tests. The nose testing package contains many of them.

### Nose

The nose testing framework has built-in assertion types implementing
`assert_almost_equal`, `assert_true`, `assert_false`, `assert_raises`,
`assert_is_instance`, and others.

~~~ {.python}
from nose.tools import assert_almost_equal
from mynum import a
assert_almost_equal(a, 2, places=2)
assert_almost_equal(a, 2, delta=0.003)
~~~

These assertions give much more helpful error messages and have much more 
powerful features than the simple assert keyword. An even more powerful sibling 
of the assertion is the _exception_. We'll learn about those in the next 
lesson.


> ## Key Points {.keypoints}
>
> -   Assertions are one line tests embedded in code.
> -   The `assert` keyword is used to set an assertion.
> -   Assertions halt execution if the argument is false.
> -   Assertions do nothing if the argument is true.
> -   The `nose.tools` package provides more informative assertions.
> -   Assertions are the building blocks of tests.
