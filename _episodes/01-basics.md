---
layout: page
title: Testing
subtitle: Basics of Testing
minutes: 5
---
}
>
> *   Understand the place of testing in a scientific workflow.
> *   Understand that testing has many forms.

The first step toward getting the right answers from our programs is to assume
that mistakes *will* happen and to guard against them.  This is called
**defensive programming** and the most common way to do it is to add alarms and
tests into our code so that it checks itself.

**Testing** should be a seamless part of scientific software development process.
This is analogous to experiment design in the experimental science world:

- At the beginning of a new project, tests can be used to help guide the 
  overall architecture of the project.
- The act of writing tests can help clarify how the software should be perform when you are done. 
- In fact, starting to write the tests _before_ you even write the software 
  might be advisable. (Such a practice is called _test-driven development_, 
  which we will discuss in greater detail [later in the lesson](09-tdd.html).)

}
>
> There are many ways to test software, such as:
>
> - Assertions
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
