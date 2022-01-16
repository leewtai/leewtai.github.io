# Variables

Sometimes we want to refer to the same quantity repeatly throughout our code.
For example, the sample size $n$ in introductory statistics is used to
calculate the average, the variance of the average, the cost
of the sample, and the expected number of records in your database.
This is when we use variables.

The main benefits of using variables
- Consistent value will be used by avoiding typos, changes at the top will change
  all following instances of the same value.
- Code would be easier to read if your variable is named `sample_size` instead of `n`

#### How to define a variable
To define a variable, simply use the `=` and have the variable name on the left and
the value you want to assign on the right.

In the following example we would say
"we've assigned the value 111 to the variable `sample_size`"

```python
sample_size = 111
```

#### Some important things to know
The right-hand-side expression will always be evaluated before the "assignment"
operation, e.g.

```python
x = 3 * 4
```
If `=` happened before `*`, then `x` **could** be 3 (almost no languages do this).
Fortunately, the assignment operation is always last so `x` will take on the value 12

#### Some convenient features in Python
Sometimes we want to have the same default value for some variables (e.g. `0`)

Python allows you to define variables in a chain
```python
a = b = 2
```

Does this work?
```python
a = 2 = b
```


## Restrictions when defining variables

There are restrictions on what your variable name can be.

One of these won't work
```python
a3 = 1
3a = 2
_a = 3
_ = 4
```

There are other restrictions but the key is to try it if you're not sure.

## Something we take for granted

In some programming languages, you have to define the "type" of the variable
when you define it. This isn't true for Python which makes it easier to read
but also allows mistakes to happen more easily, e.g. when different scripts
can assign different values to the same variable name.

```python
a = 1
a = '1'
```

## Always always always spend some time to think about variable names

Naming variables is sometimes considered one of the hardest things to do in
programming. Achieving concise, meaningful, and specific names is hard.
This is especially in large projectds but you should practice early.

#### Convention around `_`

Some people use the `_` to prevent information printed in the REPL since
algorithms can print a lot of information that swamps your REPL.

The underscore is often used by programmers to indicate something should
remain hidden or ignored when reading the code. The following is an example
of this. Don't worry about not following the code (you'll understand in the 
next topic!) This is just to show that `_` are used commonly in Python
but you should just treat it like a letter.
```python
a = "hello"
a.upper()
a.__len__()
```

## Additional References
- [LearnPython.org](https://www.learnpython.org/en/Variables_and_Types)

## Something you may not understand yet...

```python
a = 3
b = a
print(a)
print(b)
b = 4
print(a)
print(b)
```

```python
a = [1, 2]
print(a)
b = a
b[0] = -1
print(a)
print(b)
b = 3
print(a)
print(b)
```
