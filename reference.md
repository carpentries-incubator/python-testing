---
layout: page
title: Testing
subtitle: Reference
---
## [Basics of Testing](01-basics.html)

-   Tests compare that the result observed from running code is the same as what was expected ahead of time.
-   Tests should be written at the same time as the code they are testing is written.
-   Assertions and exceptions are like alarm systems embedded in the software, guarding against exceptional bahavior.
-   Unit tests try to test the smallest pieces of code possible, usually functions and methods.
-   Integration tests make sure that code units work together properly.
-   Regression tests ensure that everything works the same today as it did yesterday.

## [Assertions](02-assertions.html)

-   Assertions are one line tests embedded in code.
-   The `assert` keyword is used to set an assertion.
-   Assertions halt execution if the argument is false.
-   Assertions do nothing if the argument is true.
-   The `nose.tools` package provides more informative assertions.
-   Assertions are the building blocks of tests.

## [Exceptions](03-exceptions.html)

-   Exceptions are effectively specialized runtime tests
-   Exceptions can be caught and handled with a try-except block
-   Many built-in Exception types are available 

## [Unit Tests](04-units.html)

-   Functions are the atomistic unit of software.
-   Simpler units are easier to test than complex ones.
-   A single unit test is a function containing assertions.
-   Such a unit test is run just like any other function.
-   **Running tests one at a time is pretty tedious.** (let's use a framework instead)

## [Running Tests with Nose](05-nose.html)

-   The `nosetests` command collects and runs tests starting with `Test-`, `test_`, and similar names.
-   `.` means the test passed
-   `F` means the test failed
-   `E` encountered an error
-   `K` is a known failure
-   `S` is a purposefully skipped test

## [Edge and Corner Cases](06-edges.html)

-   Functions often fail at the edge of their range of validity
-   Edge case tests query the limits of a function's behavior
-   Corner cases are where two edge cases meet

## [Integration and Regression Tests](07-integration.html)

-   Integration tests interrogate the coopration of pieces of the software
-   Regression tests use past behavior as the expected result

## [Continuous Integration](08-ci.html)

-   Servers exist for automatically running your tests
-   Running the tests can be triggered by a GitHub pull request
-   CI allows cross platform build testing
-   A `.travis.yml` file configures a build on the travis-ci servers
-   Many free CI servers are available

## [Test Driven Development](09-tdd.html)

-   Test driven development is a common software development technique
-   By writing the tests first, the function requirements are very explicit
-   TDD is not for everyone
-   TDD requires vigilance for success (cheating leads to failure)

## [Fixtures](10-fixtures.html)

-   It may be necessary to set up "fixtures" composing the test environment.

## Glossary

*   `assert` is a keyword that halts code execution when its argument is false
*   `Exceptions` are customizeable cousin of assertions.
*   `try` is a keyword that guards a piece of code which may throw an exception.
*   `except` is a keyword used to catch and carefully handle that exception
*   `nose` is a python package with useful assertions and unit test utilities
*   `nosetests` is a command-line program that collects and runs unit tests.
*    _Unit Tests_ investigate the behavior of units of code (such as functions, classes, or data structures). 
*    _Regression Tests_ defend against new bugs, or regressions, which might appear due to new software and updates.
*    _Integration Tests_ check that various pieces of the software work together as expected.
*   _Continuous Integration_ automates the building and testing process accross platforms.
*   _Test-driven Development_ is a software development strategy in which the tests are written before the code.
