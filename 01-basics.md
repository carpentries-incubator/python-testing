---
layout: page
title: Testing
subtitle: Basics of testing
minutes: 5
---
> ## Learning Objectives {.objectives}
>
> *   Understand the place of testing in a scientific workflow.
> *   Understand that testing has many forms.

Testing should be a seamless part of scientific software development process.
The purpose of the software should be clear to anyone reading the tests. For
this reason, the purpose of the software must be clear the person writing the
test. Thus, tests should be created aroudnd the same time as the code in
qustion. Similarly, the author of the original software is often the best
person to write the tests for that software.  

At the beginning of a new project, tests can
be used to help guide the overall architecture of the project.
This is analogous to experiment design in the experimental science world.
The act of writing tests can help clarify how the software
should be performing. Taking this idea to the
extreme you could start to write the tests _before_ you even write the software
that will be
tested. Such a practice is called _test-driven development_, which we will
discuss in greater detail [later in the lesson](09-tdd.html).

> ### What Kinds of Tests Exist
> There are many ways to test software, such as:
>
> - Exceptions
> - Unit Tests
> - Regresson Tests
> - Integration Tests

*Exceptions and Assertions*: While writing code, `exceptions` and `assertions` 
can be added to sound an alarm as runtime problems come up. These kinds of 
tests, are embedded in the software iteself and handle, as their name implies, 
exceptional cases rather than the norm. 

*Unit Tests*: Unit tests investigate the behavior of units of code (such as
functions, classes, or data structures). By validating each software unit
across the valid range of its input and output parameters, tracking down
unexpected behavior that may appear when the units are combined is made vastly
simpler.

*Regression Tests*: Regression tests defend against new bugs, or regressions,
which might appear due to new software and updates. 

*Integration Tests*: Integration tests check that various pieces of the
software work together as expected. 


> ## Key Ideas {.callout}
> 
> * Tests compare that the result observed from running code is the same as what was
  expected ahead of time.
> * Tests should be written at the same time as the code they are testing is written.
> * The person best suited to write a test is the author of the original code.
> - Assertions and exceptions are like alarm systems embedded in the software, guarding against exceptional bahavior.
- * Unit tests try to test the smallest pieces of code possible, usually functions and
  methods.
> - * Integration tests make sure that code units work together properly.
> - * Regression tests ensure that everything works the same today as it did yesterday.

