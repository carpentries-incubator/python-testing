---
layout: page
title: Testing
subtitle: Design by Contract
minutes: 15
---
> ## Learning Objectives {.objectives}
>
> *   Design by Contract is a way of using Assertions for interface specification.
> *   Design by Contract defines pre-, post- and invariant conditions a function and a caller agree to obey.

In [Design by Contract](https://en.wikipedia.org/wiki/Design_by_contract), the interaction between a caller
and a library is treated as being governed by a *contract*. A contract involves three different types of requirements.

* Pre-conditions: Things that must be true before calling the function.
* Post-conditions: Things that are guaranteed to be true after the function returns.
* Invariant-conditions: Things that are guaranteed not to change during the function's execution (e.g. side effects)

**NOTE**: In Python's contracts, only pre- and post-conditions are handled.

To demonstrate the use of contracts, in the example here, we implement our own version of an integer square root
function for perfect squares, called psqrt. We define a contract that indicates the caller is required to pass an
integer value greater than or equal to zero. This is an example of a pre-condition. Next, the function will return
an integer greater than or equal to zero. This is an example of a post-condition.
The contract is defined using Python [decorator](https://www.python.org/dev/peps/pep-0318) notation.

~~~ {.python}
from math import sqrt
from contracts import contract

@contract(x='int,>=0',returns='int,>=0')
def psqrt(x):
    return int(sqrt(x))

print "Square root of perfect square 4 = %d"%psqrt(4)
~~~
~~~ {.output}
Square root of perfect square 4 = 2
~~~

Here the caller and the function obey the contract and the function call proceeds as expected. Next, let's see what
happens when we pass a negative value to the funciton.

~~~ {.python}
print "Square root of perfect square -4 = %d"%psqrt(-4)
~~~
~~~ {.output}
Traceback (most recent call last):
  File "../foo.py", line 9, in <module>
    print "Square root of perfect square -4 = %d"%psqrt(-4)
  File "<decorator-gen-1>", line 2, in psqrt
  File "/Library/Python/2.7/site-packages/PyContracts-1.7.15-py2.7.egg/contracts/main.py", line 253, in contracts_checker
    raise e
contracts.interface.ContractNotRespected: Breach for argument 'x' to psqrt().
Condition -4 >= 0 not respected
checking: >=0       for value: Instance of <type 'int'>: -4   
checking: int,>=0   for value: Instance of <type 'int'>: -4   
Variables bound in inner context:
~~~

Here, an exception is raised and some additional details indicating which condition of the contract was violated.

### Extending Contracts

Sometimes, the simple syntax for defining contracts is not sufficient. In this case, contracts can be extended by
defining a function that implements a new contract. For example, number theory tells us that all perfect squares
end in a digit of 1,4,5,6, or 9 or end in an even number of zero digits. We can define a new contract that checks
this condition

~~~ {.python}
@new_contract
def endsOk(x):
    ends14569 = x%10 in (1,4,5,6,9)
    ends00 = int(round((log(x,10)))) % 2 == 0
    if ends14569 or ends00:
        return True
    raise ValueError("%s doesn't end in 1,4,5,6 or 9 or even number of zeros"%x)
~~~

We can then use this function, *endsOk*, in a contract specification

~~~ {.python}
@contract(x='int,endsOk,>=0',returns='int,>=0')
def psqrt2(x):
    return int(sqrt(x))
~~~

Let's see what happens when we try to use this *psqrt2* function on a number that ends in an odd number of zeros.

~~~ {.python}
print "Perfect square root of 1000 = %d"%psqrt2(1000)
~~~

~~~ {.output}
Traceback (most recent call last):
  File "../foo.py", line 24, in <module>
    print "Perfect square root of 1000 = %d"%psqrt2(1000)
  File "<decorator-gen-3>", line 2, in psqrt2
  File "/Library/Python/2.7/site-packages/PyContracts-1.7.15-py2.7.egg/contracts/main.py", line 253, in contracts_checker
    raise e
contracts.interface.ContractNotRespected: Breach for argument 'x' to psqrt2().
1000 doesn't end in 1,4,5,6 or 9 or even number of zeros
checking: callable()       for value: Instance of <type 'int'>: 1000   
checking: endsOk           for value: Instance of <type 'int'>: 1000   
checking: int,endsOk,>=0   for value: Instance of <type 'int'>: 1000   
Variables bound in inner context:
~~~

### Performance Considerations

Depending on the situation, checking validity of a contract can be expensive. For example, suppose a function
is designed to perform a binary search on a sorted list of numbers. A pre-condition for the operation is that
the list it is given to search is sorted. If the list is large, checking that it is properly sorted is expensive.
In other words, contracts can impact performance. This means it is desirable to have a way to disable contract
checks. This can be accomplished either by setting an environment variable, DISABLE_CONTRACTS or by a call to
contracts.disable_all() **before** any @contracts are processed by the Python interpreter.

[Learn more about Design by Contract in Python](https://andreacensi.github.io/contracts/index.html#)
