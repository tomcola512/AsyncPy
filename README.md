# AsyncPy
Threaded python shell for asynchronous execution.

Info:


agents dict: should contain objects with a `run` method. These are evaluated every tick.


i: global increment counter


Example run:

```
AsyncPy Shell
=====
Press Enter to aquire lock
Input single line python expression or statement to be evaluated or executed

Input exit to exit



> a = Agent(lambda: i)

> agents['a'] = a
Agent output
=====
'a' >: 31
=====

Agent output
=====
'a' >: 32
=====


> b = Agent(lambda: agents['a'].run()/2 + 5)
Agent output
=====
'a' >: 33
=====

Agent output
=====
'a' >: 34
=====


> agents['b'] = b
Agent output
=====
'a' >: 35
=====

Agent output
=====
'a' >: 36
'b' >: 23
=====

Agent output
=====
'a' >: 37
'b' >: 23
=====


> 
```
