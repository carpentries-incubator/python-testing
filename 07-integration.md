---
layout: page
title: Testing
subtitle: Integration and Regression Tests
minutes: 10
---
}
>
> *   Understand the purpose of integration and regression tests
> *   Understand how to implement an integration test


## Integration Tests

You can think of a software project like a clock. Functions and classes are
the gears and cogs that make up the system. On their own, they can be of the highest
quality. Unit tests verify that each gear is well made. However, the clock still
needs to be put together. The gears need to fit with one another.

}
>
> _Integration tests_ are the class of tests that verify that multiple moving
> pieces and gears inside the clock work well together. Where unit tests
> investigate the gears, integration tests look at the position of the hands to
> determine if the clock can tell time correctly.  They look at the system as a
> whole or at its subsystems.  Integration tests typically function at a higher
> level conceptually than unit tests.  Thus, writing integration tests also
> happens at a higher level.

Because they deal with gluing code together, there are typically fewer
integration tests in a test suite than there are unit tests.  However, integration
tests are
no less important. Integration tests are essential for having adequate testing.
They encompass all of the cases that you cannot hit through plain unit testing.

Sometimes, especially in probabilistic or stochastic codes, the precise behavior
of an integration test cannot be determined beforehand.  That is OK. In these
situations it is acceptable for integration tests to verify average or aggregate
behavior rather than exact values. Sometimes you can mitigate nondeterminism by saving
seed values to a random number generator, but this is not always going to be possible.
It is better to have an imperfect integration test than no integration test
at all.


As a simple example, consider the three functions `a()`, `b()`,
and `c()`.  The `a()` function adds one to a number, `b()` multiplies a number
by two, and `c()` composes them.  These functions are defined as follows:

~~~
def a(x):
    return x + 1

def b(x):
    return 2 * x

def c(x):
    return b(a(x))
~~~
{: .python}

The `a()` and `b()` functions can each be unit tested because they each do one thing.
However, `c()` cannot be truly unit tested because all of the real work is farmed
out to `a()` and `b()`. Testing `c()` will be a test of whether `a()` and
`b()` can be integrated together.

Integration tests still follow the pattern
of comparing expected results to observed results. A sample `test_c()` is implemented here:

~~~
from mod import c

def test_c():
    exp = 6
    obs = c(2)
    assert obs == exp
~~~
{: .python}

Given the lack of clarity in what is defined as a code unit, what is considered an
integration test is also a little fuzzy.  Integration
tests can range from the extremely simple
(like the one just shown) to the very complex.
A good delimiter, though, is in opposition to the unit
tests.  If a function or class only combines two or more unit-tested pieces of code, then you need an integration test. If a function implements new behavior
that is not otherwise tested, you need a unit test.

The structure of integration tests is very similar to that of unit tests. There
is an expected result, which is compared against the observed value. However,
what goes in to creating the expected result or setting up the code to run
can be considerably more complicated and more involved.  Integration tests
can also take much longer to run because of how much more work they do. This is a
useful classification to keep in mind while writing tests. It helps separate out
which test should be easy to write (unit) and which ones may require more
careful consideration (integration).

Integration tests, however, are not the end of the story.

## Regression Tests

Regression tests are qualitatively different from
both unit and integration tests. Rather than assuming that the test author knows what
the expected result should be, regression tests look to the past for the
expected behavior. The expected
result is taken as what was previously computed for the same inputs.

}
>
> Regression tests assume that the past is "correct." They are great for
> letting developers know when and how a code base has changed. They are not
> great for letting anyone know why the change occurred. The change between
> what a code produces now and what it computed before is called a
> _regression_.

Like integration tests, regression tests tend to be high level. They often
operate on an entire code base. They are particularly common and useful for
physics simulators.

A common regression test strategy spans multiple code versions. Suppose there
is an input file for version X of a simulator. We can run the simulation
and then store the output file for later use, typically somewhere accessible online.
While version Y is being developed, the test suite will automatically download
the output for version X, run the same input file for version Y, and then
compare the two output files.  If anything
is significantly different between them, the test fails.

In the event of a regression test failure, the onus is on the current developers
to explain why.  Sometimes there are backward-incompatible changes that had to be
made. The regression test failure is thus justified, and a new version of the
output file should be uploaded as the version to test against.
However, if the test fails because the physics is wrong, then the developer should
fix the latest version of the code as soon as possible.

Regression tests can and do catch failures that integration and unit tests miss.
Regression tests act as an automated short-term
memory for a project.  Unfortunately, each project will have a slightly different
approach to regression testing based on the needs of the software. Testing
frameworks provide tools to help with building regression tests but do not offer
any sophistication beyond what has already been seen in this chapter.

Depending on the kind of project, regression tests may or may not be needed.
They are only truly needed if the project is a simulator.
Having a suite of
regression tests that cover the range of physical possibilities is vital
to ensuring that the simulator still works.
In most other cases, you can get away with only having unit and integration
tests.

While more test classifications exist for more specialized situations, we have covered
what you will need to know for almost every situation in computational physics.
