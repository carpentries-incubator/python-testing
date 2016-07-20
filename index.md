---
layout: page
title: Testing
---

> ## Prerequisites {.prereq}
>
> In this lesson we use a python library called py.test. 
> Basic understanding of python variables and functions are a necessary
> prerequisite.
> Some previous experience with the shell is expected,
> *but isn't mandatory*.


> ## Getting ready {.getready}
>
> Nothing to do: you're ready to go!

## Topics

1.  [Basics of Testing](01-basics.html)
2.  [Assertions](02-assertions.html)
3.  [Exceptions](03-exceptions.html)
4.  [Unit Tests](04-units.html)
5.  [Running Tests with py.test](05-pytest.html)
6.  [Edge and Corner Cases](06-edges.html)
7.  [Integration and Regression Tests](07-integration.html)
8.  [Continuous Integration](08-ci.html)
9.  [Test Driven Development](09-tdd.html)
10. [Fixtures](10-fixtures.html)

Before relying on a new experimental device, an experimental scientist always
establishes its accuracy. A new detector is calibrated when the scientist
observes its responses to to known input signals. The results of this
calibration are compared against the _expected_ response. **An experimental
scientist would never conduct an experiment with uncalibrated detectors - the
that would be unscientific. So too, simulations and analysis with untested
software do not constitute science.**

> ## How Do You Know Your Code is Right? {.callout}
>
> **You can only know by testing it.** Software bugs are hiding in all 
> nontrivial software. Testing is the process by which those bugs are 
> systematically exterminated before they have a chance to cause a paper 
> retraction. In software tests, just like in device calibration, expected 
> results are compared with observed results in order to establish accuracy. 

The collection of all of the tests for a given code is known as the _test
suite_. You can think of the test suite as a bunch of pre-canned experiments
that anyone can run. If all of the test pass, then the code is at least
partially trustworthy. If any of the tests fail then the code is known to be
incorrect with respect to whichever case failed.  After this lesson, you will 
know to not trust software when its tests do not _cover_ its claimed 
capabilities and when its tests do not pass.

> ## But How Close is Close Enough? {.callout}
>
> In the same way that your scientific domain has expectations concerning 
> experimental accuracy, it likely also has expectations concerning allowable 
> computational accuracy. These considerations should surely come into play 
> when you evaluate the acceptability of your own or someone else's software.

In most other programming endeavors, if code is fundamentally wrong
- even for years at a time - the impact of this error can be relatively small.
Perhaps a website goes down, or a game crashes, or a days worth of writing is
lost to a bug in your word processor. Scientific code, on the other hand,
controls planes, weapons systems, satellites, agriculture, and most importantly
scientific simulations and experiments. If the software that governs the
computational or physical experiment is wrong, then disasters (such as false
claims in a publication) will result.

This is not to say that scientists have a monopoly on software testing, simply
that software cannot be called _scientific_ unless it has been validated.

> ## Why Untested Code is Legacy Code {.callout}
>
> In *[Working Effectively with Legacy Code](http://www.amazon.com/Working-Effectively-Legacy-Michael-Feathers/dp/0131177052/)*,
> Michael Feathers defines legacy 
> code as "any code without tests". This definition draws on the fact that 
> after its initial creation, tests provide a powerful guide to other 
> developers (and to your forgetful self, a few months in the future) about how 
> each function is meant to be used. Without runnable tests to provide examples 
> of code use, even brand new programs are unsustainable.

Testing is the calibration step of the computational simulation and analysis
world: it lets the scientist trust their own work on a fundamental level and
helps others to understand and trust their work as well. 
Furthermore, tests help you to never fix a bug a second time. Once a bug has
been caught and a test has been written, that particular bug can never again
re-enter the codebase unnoticed. So, whether motivated by principles or a 
desire to work more efficiently, all scientists can benefit from testing.

> ## Effective Computation In Physics {.callout}
>
> Note that this testing lesson was adapted from the Testing chapter in 
> *[Effective Computation In Physics](http://physics.codes)*
> by Anthony Scopatz and Kathryn Huff.
> It is often quoted directly.


## Other Resources

*   [Reference](reference.html)
*   [Discussion](discussion.html)
*   [Instructor's Guide](instructors.html)
