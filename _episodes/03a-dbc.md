---
title: Design by Contract
teaching: 5
exercises: 10
questions:
- "What is Design by Contract?"
objectives:
- "Learn to use Python contracts, PyContracts."
- "Learn to define simple and complicated contracts."
- "Learn about pre-, post- and invariant- conditions of a contract."
keypoints:
- "Design by Contract is a way of using Assertions for interface specification."
- "Pre-conditions are promises you agree to obey when calling a function."
- "Post-conditions are promises a function agrees to obey returning to you."
---

In [Design by Contract](https://en.wikipedia.org/wiki/Design_by_contract), the interaction between 
an application and functions in a library is managed, metaphorically, by a *contract*. A contract for a
function typically involves three different types of requirements.

* Pre-conditions: Things that must be true before a function begins its work.
* Post-conditions: Things that are guaranteed to be true after a function finishes its work.
* Invariant-conditions: Things that are guaranteed not to change as a function does its work.

**Note**: In Python contracts, only pre- and post-conditions are handled.

In the examples here, we use [PyContracts](https://andreacensi.github.io/contracts/index.html#) which uses
Python [decorator](https://www.python.org/dev/peps/pep-0318) notation. In addition, to simplify the examples,
the following imports are assumed...

~~~ {.python}
from math import sqrt
from contracts import contract, new_contract
~~~

To demonstrate the use of contracts, in the example here, we implement our own version of an integer square root
function for perfect squares, called `perfect_sqrt`. We define a contract that indicates the caller is required
to pass an integer value greater than or equal to zero. This is an example of a pre-condition. Next, the function
is required to return an integer greater than or equal to zero. This is an example of a post-condition.

~~~ {.python}
@contract(x='int,>=0',returns='int,>=0')
def perfect_sqrt(x):
    retval = sqrt(x)
    iretval = int(retval)
    return iretval if iretval == retval else retval
~~~

Now, lets see what happens when we use this function to compute square roots.

~~~ {.output}
>>> perfect_sqrt(4)
2
>>> perfect_sqrt(81)
9
~~~

Values of 4 and 81 are both integers. So, in these cases the caller has obeyed the pre-conditions of the contract.
In addition, because both 4 and 81 are perfect squares, the function correctly returns their integer square root.
So, the funtion has obeyed the post-conditions of the contract.

Now, lets see what happens when the caller fails to obey the pre-conditions of the contract by passing a negative
number.

~~~ {.output}
>>> perfect_sqrt(-4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<decorator-gen-2>", line 2, in perfect_sqrt
  File "/Library/Python/2.7/site-packages/PyContracts/contracts/main.py", line 253, in contracts_checker
    raise e
contracts.interface.ContractNotRespected: Breach for argument 'x' to perfect_sqrt().
Condition -4 >= 0 not respected
checking: >=0       for value: Instance of <type 'int'>: -4   
checking: int,>=0   for value: Instance of <type 'int'>: -4   
Variables bound in inner context:
~~~

An exception is raised indicating a failure to obey the pre-condition for passing a value greather than or equal to zero.
Next, lets see what happens when the function cannot obey the post-condition of the contract.

~~~ {.output}
>>> perfect_sqrt(83)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<decorator-gen-2>", line 2, in perfect_sqrt
  File "/Library/Python/2.7/site-packages/PyContracts/contracts/main.py", line 264, in contracts_checker
    raise e
contracts.interface.ContractNotRespected: Breach for return value of perfect_sqrt().
.
.
.
checking: Int|np_scalar_int|np_scalar,array(int)      for value: Instance of <type 'float'>: 9.1104335791443   
checking: $(Int|np_scalar_int|np_scalar,array(int))   for value: Instance of <type 'float'>: 9.1104335791443   
checking: int                                         for value: Instance of <type 'float'>: 9.1104335791443   
checking: int,>=0                                     for value: Instance of <type 'float'>: 9.1104335791443   
Variables bound in inner context:
~~~

For the value of 83, although the caller obeyed the pre-conditions of the contract, the function does not
return an integer value. It fails the post-condition and an exception is raised.

### Extending Contracts

Sometimes, the simple built-in syntax for defining contracts is not sufficient. In this case, contracts can
be extended by defining a function that implements a new contract. For example, number theory tells us that
all perfect squares end in a digit of 1,4,5,6, or 9 or end in an even number of zero digits. We can define
a new contract that checks this condition

~~~ {.python}
@new_contract
def ends_ok(x):
    ends14569 = x%10 in (1,4,5,6,9)
    ends00 = int(round((log(x,10)))) % 2 == 0
    if ends14569 or ends00:
        return True
    raise ValueError("%s doesn't end in 1,4,5,6 or 9 or even number of zeros"%x)
~~~

We can then use this function, `ends_ok`, in a contract specification

~~~ {.python}
@contract(x='int,ends_ok,>=0',returns='int,>=0')
def perfect_sqrt2(x):
    return int(sqrt(x))
~~~

Let's see what happens when we try to use this `perfect_sqrt2` function on a number that ends in an
odd number of zeros.

~~~ {.output}
>>> perfect_sqrt2(49)
7
>>> perfect_sqrt2(1000)
Traceback (most recent call last):
  File "../foo.py", line 24, in <module>
    print "Perfect square root of 1000 = %d"%perfect_sqrt2(1000)
  File "<decorator-gen-3>", line 2, in perfect_sqrt2
  File "/Library/Python/2.7/site-packages/PyContracts/contracts/main.py", line 253, in contracts_checker
    raise e
contracts.interface.ContractNotRespected: Breach for argument 'x' to perfect_sqrt2().
1000 doesn't end in 1,4,5,6 or 9 or even number of zeros
checking: callable()       for value: Instance of <type 'int'>: 1000   
checking: ends_ok          for value: Instance of <type 'int'>: 1000   
checking: int,ends_ok,>=0  for value: Instance of <type 'int'>: 1000   
Variables bound in inner context:
~~~

### Performance Considerations

Depending on the situation, checking validity of a contract can be expensive. For example, suppose a function
is designed to perform a binary search on a sorted list of numbers. A pre-condition for the operation is that
the list it is given to search is sorted. If the list is large, checking that it is properly sorted is expensive.
In other words, contracts can negatively impact performance. For this reason, it is desirable for callers to
have a way to disable contract checks to avoid always paying whatever performance costs they incur. This can
be accomplished either by setting an environment variable, DISABLE_CONTRACTS or by a call to
contracts.disable_all() **before** any `@contracts` statements are processed by the Python interpreter.
This allows developers to keep the checks in place while they are developing code and then disable them once
they are sure their code is working as expected.

Contracts are most helpful in the process of _developing_ code. So, it is often good practice to write
contracts for functions _before_ the function implementations. Later, when development is complete and
performance becomes important, contracts can be disabled. In this way, contracts are handled much like
assertions. They are useful in developing code and then disabled once development is complete.

[Learn more about Design by Contract in Python](https://andreacensi.github.io/contracts/index.html#)
