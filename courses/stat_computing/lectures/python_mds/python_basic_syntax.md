# Python Basic Syntax

## Using Python as a calculator
Python can perform all the functionalities that advanced calculators
can perform.

```python
1 + 1
100 * 2
10 ** 2  # exponentiate
```

A successful execution in the REPL will often output the result of the computation
and "print" the final results just after the code.

Later, some computations will
produce results with multiple attributes, e.g. a model's parameters, inputs, and runtime.
What gets printed in these cases can vary widely so you shouldn't assume you'll be able
to "view everything" when you're running code.
Instead you should/will learn to __ask__ for what is available!


## Python cares about indentation at the front of the line
One unique characteristic about Python is that its syntax forces us to
write "neater" code. It enforces this by interpreting the empty spaces
in front of the code as part of the command.

See which of the following will "break"
```python
1+1
1 + 1
1 +     1
    1 + 1
```

If you're using **iPython**, you may not see an error in any of the commands
above.


## Reading error messages
Python's error messages often have the word "Error" in them.
This means that Python encountered a problem that forced the code execution
to stop somewhere in the code but it may not be obvious what has and has
not been executed.

Below we have two examples where we try to add the number `1` to the
character `"1"`, notice how the errors are different!

```python
>>> 1 + "1"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
>>> 
>>> 1 + 
  File "<stdin>", line 1
    1 + 
       ^
SyntaxError: invalid syntax
```

As a beginner, you should focus on:
- the error type, e.g. "TypeError". Knowing the category of error can quickly
  help us understand the issue in our code.
- the error message, e.g. "unsupported operand type(s) for +: 'int' and 'str'"
- Python's best guess at **where** the error occurred, e.g. `line 1` will
  usually be the case for most REPL commands. This would be more helpful
  if your code were in a script.

## Dealing with error messages
You should try to embrace error messages early on. Expert
coders make errors all the time and the messages are really there
to guide you instead of intimidate you.

## The print() function
Similar to how calculators can perform `log(1)`, Python has some built-in
functions ready to use. One of the most useful ones is `print()`.

It's most useful when you're not sure of the value of a variable.
In particular, `print()` will accept numeric, character values, **and more**.
This may seem trivial for now but later you will see that most
functions are strict about the type of inputs it will accept. 

Try running the code below line by line, then try to "copy&paste" blocks
of the code. See how things may be different in a REPL.

```python
print('hello world!')
x = 'hello universe!'
print(x)

x = 1.3
y = x * 3
z = x * y / 13
print(z)

print('hello', z)
```

Notice that our last `print()` function took 2 inputs that were separated by
a comma.

#### Writing comments in code
Sometimes we write comments into our code to remind ourselves of some subtle
choices. Comments will be ignored by Python but stay in the script as a
descriptive reminder.

```python
audience = 'class'
# The audience should come from the class list
print('hello {}'.format(audience))
```


## Additional references
- [LearnPython.org's HelloWorld](https://www.learnpython.org/en/Hello%2C_World%21)
- [Guru99's HelloWorld](https://www.guru99.com/creating-your-first-python-program.html)


{% include lib/mathjax.html %}
