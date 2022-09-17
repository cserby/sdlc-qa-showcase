# Question

The output of `Writer` is not clearly specified. There might be multiple ints received before a `.tick` call happens. In
this case what is `Writer` supposed to output? The Spec has the following wording:

> Writes any received number to the console

The following interpretations are possible:

- any numbers received since the previous tick
- any numbers received since system startup
- the last number received before the tick

It's also unclear if printing a number to the console should _consume_ that number, or `Writer` should _always_ (as long as it has received at least one) output a number on `.tick`.

# Context

... (describe what the real world User Story is, how will the output be used?)

# Consequences

...

# Decision

`Writer` will output the last integer received before the `.tick`, and that number will be consumed. Subsequent `.tick`s will produce no number, unless `.receive_int` was called in-between.
