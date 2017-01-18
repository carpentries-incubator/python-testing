---
layout: lesson
root: .
---

In this lesson we use a Python library called pytest. 
Basic understanding of Python variables and functions are a necessary
prerequisite.
Some previous experience with the shell is expected, *but isn't mandatory*.

> ## Prerequisites
>
> Nothing to do: you're ready to go!
{: .prereq}

Before relying on a new experimental device, an experimental scientist always
establishes its accuracy. A new detector is calibrated when the scientist
observes its responses to to known input signals. The results of this
calibration are compared against the _expected_ response.

**An experimental scientist would never conduct an experiment with uncalibrated detectors - the
that would be unscientific. So too, simulations and analysis with untested
software do not constitute science.**


> ## You only know what you test
>
> **You can only know by testing it.** Software bugs are hiding in all
> nontrivial software. Testing is the process by which those bugs are
> systematically exterminated before they have a chance to cause a paper
> retraction. In software tests, just like in device calibration, expected
> results are compared with observed results in order to establish accuracy.
{: .callout}

The collection of all of the tests for a given code is known as the _test
suite_. You can think of the test suite as a bunch of pre-canned experiments
that anyone can run. If all of the test pass, then the code is at least
partially trustworthy. If any of the tests fail then the code is known to be
incorrect with respect to whichever case failed.  After this lesson, you will
know to not trust software when its tests do not _cover_ its claimed
capabilities and when its tests do not pass.

> ## Managing Expectations
>
> In the same way that your scientific domain has expectations concerning
> experimental accuracy, it likely also has expectations concerning allowable
> computational accuracy. These considerations should surely come into play
> when you evaluate the acceptability of your own or someone else's software.
{: .callout}

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

> ## Code without tests...doesn't exist!
>
> In *[Working Effectively with Legacy Code][feathers-legacy-code]*,
> Michael Feathers defines legacy code as "any code without tests". This definition
> draws on the fact that after its initial creation, tests provide
> a powerful guide to other developers (and to your forgetful self, a few months
> in the future) about how each function is meant to be used. Without runnable
> tests to provide examples of code use, even brand new programs are unsustainable.
{: .callout}

Testing is the calibration step of the computational simulation and analysis
world: it lets the scientist trust their own work on a fundamental level and
helps others to understand and trust their work as well.
Furthermore, tests help you to never fix a bug a second time. Once a bug has
been caught and a test has been written, that particular bug can never again
re-enter the codebase unnoticed. So, whether motivated by principles or a
desire to work more efficiently, all scientists can benefit from testing.

> ## Where these lessons are from
>
> Note that this testing lesson was adapted from the Testing chapter in
> *[Effective Computation In Physics](http://physics.codes)*
> by Anthony Scopatz and Kathryn Huff.
> It is often quoted directly.
{: .callout}

[feathers-legacy-code]: http://www.amazon.com/Working-Effectively-Legacy-Michael-Feathers/dp/0131177052/
