# Overview

This is the Requirement Specification document for the application as described by the Product Owner.

# IMicroComponent

A `MicroComponent` (MC) is a class that can receive/send integer and respond to when the component
framework ticks.

`MicroComponent`s implement the following interface:

```
interface IMicroComponent {
    //The sendFunc is to be invoked when the component wants to output data
    function initialize(sendFunc: Int->Void) : Void;
    function receiveInt(value: Int) : Void;
    function tick(timeStep: Int) : Void;
}
```

A `MicroComponent` can both receive input from multiple sources and send to multiple targets.

# MicroComponents

Implement classes of MCs according to this spec:

| Name      | Specification                                                                       |
| --------- | ----------------------------------------------------------------------------------- |
| `Sender`  | Send the current timeStep when ticked                                               |
| `Adder`   | When two numbers have been receiver send the sum of the numbers                     |
| `Divider` | When two numbers have been received send the second number divided by the first one |
| `Writer`  | Writes any received number to the console                                           |

# Application

In an application create a network of component instances and connections between them as shown here:

| Inputs                 | Instance    | Outputs                |
| ---------------------- | ----------- | ---------------------- |
|                        | `Sender#0`  | `Adder#0`, `Divider#0` |
| `Sender#0`             | `Adder#0`   | `Divider#0`            |
| `Sender#0`, `Adder#0`  | `Divider#0` | `Writer#0`             |
| `Adder#0`, `Divider#0` | `Writer#0`  |                        |

Tick the components for time 0 to 4 and capture the output produced by the writer.

> Note: Depending on the design decisions you make the output could change. There is _not_ a single correct
> output.
