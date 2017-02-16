---
title: Exceptions
teaching: 10
exercises: 0
questions:
- "How do I capture errors that I do not anticipate?"
objectives:
- "Understand that exceptions are effectively specialized runtime tests"
- "Learn when to use exceptions and what exceptions are available"
keypoints:
- "Exceptions are effectively specialized runtime tests"
- "Exceptions can be caught and handled with a try-except block"
- "Many built-in Exception types are available"
---

Exceptions are more sophisticated than assertions. They are the standard error 
messaging system in most modern programming languages.  Fundamentally, when an 
error is encountered, an informative exception is 'thrown' or 'raised'.

For example, instead of the assertion in the case before, an exception can be
used.

~~~
def mean(num_list):
    if len(num_list) == 0 :
      raise Exception("The algebraic mean of an empty list is undefined.\
      	    	       Please provide a list of numbers")
    else :
      return sum(num_list)/len(num_list)
~~~
{: .python}

Once an exception is raised, it will be passed upward in the program scope.
An exception be used to trigger additional error messages or an alternative
behavior. rather than immediately halting code
execution, the exception can be 'caught' upstream with a try-except block.
When wrapped in a try-except block, the exception can be intercepted before it reaches
global scope and halts execution.

To add information or replace the message before it is passed upstream, the try-catch
block can be used to catch-and-reraise the exception:

~~~
def mean(num_list):
    try:
        return sum(num_list)/len(num_list)
    except ZeroDivisionError as detail :
        msg = "The algebraic mean of an empty list is undefined. Please provide a list of numbers."
        raise ZeroDivisionError(detail.__str__() + "\n" +  msg)
~~~
{: .python}

Alternatively, the exception can simply be handled intelligently. If an
alternative behavior is preferred, the exception can be disregarded and a
responsive behavior can be implemented like so:

~~~
def mean(num_list):
    try:
        return sum(num_list)/len(num_list)
    except ZeroDivisionError :
        return 0
~~~
{: .python}

If a single function might raise more than one type of exception, each can be
caught and handled separately.

~~~
def mean(num_list):
    try:
        return sum(num_list)/len(num_list)
    except ZeroDivisionError :
        return 0
    except TypeError as detail :
        msg = "The algebraic mean of an non-numerical list is undefined.\
               Please provide a list of numbers."
        raise TypeError(detail.__str__() + "\n" +  msg)
~~~
{: .python}

> ## Remember
>
> 1. Think of some other type of exception that could be raised by the try 
> block.
> 2. Guard against it by adding an except clause.
> 3. Use the mean function in three different ways, so that you cause each
> exceptional case.
{: .callout}

Exceptions have the advantage of being simple to include and powerfully helpful
to the user. However, not all behaviors can or should be found with runtime
exceptions. Most behaviors should be validated with unit tests.
