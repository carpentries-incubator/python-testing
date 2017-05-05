---
layout: page
title: Testing
subtitle: Discussion
---

## Frequently Asked Questions

### Why doesn't Travis-CI run my tests?

A common problem in the [Continuous Integration](./08-ci.html) part of this 
lesson is that Travis-CI does not run the tests in the version-controlled
repository. One thing to watch out for is that Travis-CI is *very* picky about
the format of the `.travis.yaml` file, but other problems are also possible.
Some of these, and how they can be fixed, are outlined below.

* The `.travis.yml` file is malformed. This results in an error message
`ERROR: An error occured while trying to parse your .travis.yml file` and
the test is recorded as "canceled". Try using
[https://lint.travis-ci.org/](https://lint.travis-ci.org/).
This should point to the line of the error and give a more useful error
message. Try to fix the error, commit and push the fixed `.travis.yml` file,
and push to GitHub to rerun the tests.

* The tests fail with the message `The command "rake" exited with 1.` at the
end of the log file. This indicates that Travis attempted to run the tests
for software written in Ruby. This is the default for Travis and probably means
that the `.travis.yaml` file has not been found. One reason for this may be
that the first dot has been missed. Check with `ls -a` and if this is the case
use the `git mv` command to rename the file, then `git commit` and `git push`.
This should trigger the tests to run again.

* The tests don't run at all. One reason for this is that Travis has not "seen"
changes pushed to GitHub, for example if the configuration files are pushed
before Travis is linked to the GitHub account. Try to fix this by making a 
minor change to a file, then committing and pushing the change.
