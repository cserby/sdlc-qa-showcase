# Overview

This is a Showcase project with all the QA bells and whistles.

# Quality Gates in the SDLC

Throughout the Software Development process (and extending to the whole Software Development Lifecycle),
there are several points where defining quality gates, thus
get Quality Assurance team involved brings benefits. These are outlined in the sections below.

## Requirement Engineering

It's beneficial if QA participates in the Requirement Engineering processes, for example
by doing Requirement Reviews.

This helps by:

- clearing up misunderstanding, vague wording
- introspection of interfaces, APIs, data models can reveal errors already in this early stage
- QA can call attention to observability, testability aspects of the requirements

For example, reviewing the Requirement Specifications in [Requirement Specification](docs/REQUIREMENTS.md),
I would have posed the following questions:

- It was unclear to me (traces visible in git history) if the `MicroComponent` performs its logic when `.receive_int` is called, or
  only on `.tick`. The `IMicroComponent` interface suggests the latter, as if the former were the case
  it'd basically describe a Union Type, where each implementation only ever uses one function or the other.
- The output of `Writer` is not clearly specified. There might be multiple ints received before a `.tick` call happens. In
  this case what is `Writer` supposed to output? The Spec has the following wording:

  > Writes any received number to the console

  The following interpretations are possible:

  - any numbers received since the previous tick
  - any numbers received since system startup
  - the last number received before the tick

### Version control

I suggest storing the Requirement Specification documents alongside other project documentation, the source
code and the test automation code in the same version control repository.

Here, I stored [Requirement Specification](docs/REQUIREMENTS.md). This has the following benefits:

- Docs need to go through the same review processes as source code does in order to be accepted into the repository
  - This allows all users of the repository to be able to review, comment, suggest modifications
- Docs are always available, can be consulted by anyone working on the project, at any time
- If updates are needed, they can be done on the same feature branch where the resulting code and test modifications
  will be performed

## System Design

In System Design phase the following documents need be produced in high quality:

- Architecture diagrams
- Glossary on commonly used terms
- Data models
- API definitions

For the same reasons outlined for requirement specifications, I prefer storing the System Design documentation
(for example in the [ADR](https://github.com/joelparkerhenderson/architecture-decision-record) format) in the
project repository.

These documents going through the standard branch-review-merge procedures, helps various stakeholders, among others
QA to get involved, and provide valuable feedback on:

- Clean, testable, observable API designs
- Clean data structures

I would have posed the following questions in a System Design review:

- It's unclear from the Requirement Specs if we need to design a synchronous or an asynchronous system.

  As the
  note in the Spec points out, the ordering of the `.send_func` calls influences the output of the system, this
  design choice would have fundamental consequences to the ordering of events, and thus the system behavior.

  The
  Requirement Specification document has no information on the original User Stories, thus if in doubt, we'd need
  to circle back to those in order to be able to make this choice. (In my implementation I went for the simplest
  possible solution.)

During implementing the solution in this project - lacking a feedback loop to Requirement Engineering -
I needed to make a few assumptions as regards to the Requirement Specifications, which I recorded in [ADRs](docs/adr/).

## Implementation

For the long-term habitability, reviewability and thus eventually the quality of the codebase it's highly
valuable to set out some guidelines on how contributions should be made. This entails guidelines on:

- Branching, merging strategies
- Commit message formatting
  - Language constructs
  - Links to tasks in task management tools
- Code formatting
  - Variable naming
  - Styling (editor settings)

All these guidelines should be outlined in a [Contribution Guidelines](docs/CONTRIBUTE.md) document, together
with instructions on how to set up the development environment in order to help with adhering to the guidelines.

### Static Code Analysis

Adherence to the contribution guidelines, and basic sanity checks (for example on typing) can, and should be performed
automatically, using Static Code Analysis tools.

In this project I set up `black` for formatting and linting, and `mypy` for type checking. These tools are run automatically,
as the first steps of the CI/CD pipeline. It'd be possible to require running these tools by setting up git hooks, but eventually

- in order to ensure they're run - they'd need to be run in the pipeline as well (git hooks can be circumvented).

Many more kinds of SCA tools are available, for example one could set up additional measurements for:

- code complexity
- code duplication
- dead code detection
- ...

These of course incur additional costs, so the decision about if they're needed should be taken based on analysis of the
existing code-base.

#### Reviews / VCS usage

The guidelines for using git as the version control system should describe a branch-review-merge strategy that should:

- define `main` branch as protected, thus disallowing direct pushes
- this'd ensure that all commits being made to `main` need to pass through review (Pull Request review in case of GitHub),
  and be accepted afterwards (at least be seen by four eyes - I'd also suggest having QA on the reviews as optional approvers, as
  long as possible)

As described above, all documentation, production code and test code should follow the same strategy, and thus get their output
stored - after being accepted in review - in the same repository.

### Low-level testing

I deliberately avoid using the terms Unit/Integration testing, as I've seen it create more confusion than value. I use the term
Low-level testing to refer to white-box testing activities, where mocking on the code-level is required. Should it target the
function/class/module/application level doesn't really matter, as the goal of these activities are to ensure that the code
produced functions as intended by the developer.

For instance in this project, I have `tests/components`, which in the classical sense I'd call unit tests, whereas
`test/test_network.py` would fall into the category of integration testing.

In my opinion low-level testing should be done during development, and thus is the developers' responsibility. This'd make sure
that the produced code is structured in an observable/testable way.

I suppose we're all aware of the controversies and debates about the use of code coverage as a KPI, however - because it is easy
to measure, and observe - if treated as a tool, and not as a goal, it can be a good pragmatic option.

Setting a target value for the code coverage measurment is not easy at all. Going for 100% is not feasible or desirable in most
projects due to its (short and long-term) costs, and low ROI. The golden spot needs to be hit, that fits the project and the team
best, most cases it'd be somewhere above 70%, but would need to be adjusted in iterations, while the sweet spot is hit.

This project is set up to have test coverage measured as part of the CI/CD pipeline. Additionally to the calculation and display
of the results, it'd be possible to set the measurement and the CI/CD pipeline in a way, that it'd not allow any deterioration of
the previously achieved test coverage value ([Ratcheting](https://robertgreiner.com/continuous-code-improvement-using-ratcheting/)).

### Acceptance testing

I use the term Acceptance testing (could be High-level testing as opposing to Low-level testing) to describe testing activities where
a black-box approach is taken, approaching the system under test from an end-user/product perspective. The goal of these activities
is to ensure that the product produced satisfies the end user needs captured in the User Stories.

Acceptance testing is costly, it's significantly slower then low-level testing, thus special care needs to be taken in order to keep the
execution times low. Thus I suggest full automation for the regression test set, being integrated into the CI/CD pipeline. This can be
easily achievable if the following criteria are met:

- ephemeral deployment environments are fast to be created (for example by using docker-compose)
- test cases are kept independent from each other (ephemeral users are created with no previous state)
- test cases are run parallel to each other

The procedure for creating ephemeral environments fast will provide return on investment in the development phase as well, as it allows
for newly developed features to be quickly validated by manual checks performed by the developers, or even showcasing/demoing to project
stakeholders.

Acceptance testing should incorporate input and output validation on all external facing APIs. One useful technique I usually use is
validation of API requests and responses towards established data shapes, by the means of using a strict serializer / deserializer library
(e.g. [dataclasses-json](https://github.com/lidatong/dataclasses-json) in Python for JSON-based APIs).

For release testing extra manual checks covering the lower risk user paths might be needed, in order to extend the coverage on the highest
risks provided the automated regression set. The test definitions (checklists) for these activities should be stored in the same
repository alongside the other project documentation.

As the User Stories are not available, it was not possible to set up Acceptance testing for this project.

### Non-functional testing

Due to its complexity and thus cost, and also the fact that the necessary approaches vary highly based on the actual project, I often
see this aspect of Quality Assurance being performed on an ad-hoc basis.

However if we're able to set up ephemeral environments quick, and have understanding of the real-world usage patterns of our product,
the tools exist for measuring basic performance characteristics automatically, even as a step integrated into the CI/CD pipeline.

These checks are by nature orders of magnitude slower than other steps in the pipeline (need to run traffic simulation
for minutes, in order to get sensible resource usage charts), careful consideration needs to be taken where in the merge/release process
they should be run. They most probably bring no value when run on each commit, but rather slow down the feedback provided by CI/CD.

## CI/CD

With their understanding of all the above quality gates and efforts, QA can be instrumental in defining and setting up a performant
CI/CD pipeline, that gives fast, precise feedback to the development team on the actual status of their product.

In order to bring the most value, the pipeline needs to be optimized for:

- parallelization of tasks that can be performed independent from each other (like low-level testing and acceptance testing steps)
- creating artifacts once, and re-using them in subsequent steps (like dependency caching)
- failing fast (like not waiting for an acceptance testing job to finish, if code linting job fails)

This project showcases a [CI/CD pipeline](.github/workflows/pipeline.yaml) set up using GitHub actions, performing the following:

- Code linting, styling check
- Type checking
- Parallelization of the above two
- Dependency caching
- Low-level testing with
  - Code coverage measurement (ratcheting is not set up)
  - Reporting of the results

## Ops/Support

By performing activities related to all above quality gates, QA tends to accummulate a very good understanding of the behavior of the
product they're working on from multiple aspects (product requirements, system design, non-functional characteristics), which can be
well utilized in post-deployment phases of the product lifecycle.

For example QA can help in setting up measurements/charts/alerts on the resource utilization aspects.

QA can also help Support out in complex investigations having all the tools necessary to model exotic setups and situations,
and also the know-how in reading product logs, and information from alternative measurement points of the system.
