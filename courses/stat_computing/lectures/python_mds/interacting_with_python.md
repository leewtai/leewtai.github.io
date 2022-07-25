# Interacting with Python

## Some basics about folder structure
If you're new to computing with data, you need to know the "location" of
- Where is your data
- Where is Python, i.e. the program that will read the data
- Where is the code or your "working directory", i.e. the commands for
  the program to execute

All files (data or programs) are organized by folders (e.g. Downloads
vs Documents vs Desktop) on modern operating
systems (e.g. MacOS and Windows). Most beginners will encounter problems
because they often don't know where one of those 3 locations.

Another important topic is "permissions" related to these files if
you are encountering further problems.

Ask a TA or Google online to learn about these concepts.

## The different modes of working with Python
Python enables one to communicate commands to the
computer. You'll write commands, code, that Python can
interpret into commands for the computer to execute.

To interact with Python, there are several different modes that we
list below:
- Interacting with the REPL
- Writing script then executing them
- Notebooks (in between REPL and scripts)

#### Interacting with the REPL
The read-evaluate-print loop (REPL) is the interface that responds to
every command you type immediately.

The REPL is most commonly found by executing `python` in the command line.
You can directly type code into the REPL, i.e. the space after `>`.

<img src="images/command_line.png" alt="REPL demo" width='600'>

**Flaws**:
- The commands in the REPL are not saved to a file so it is hard
  to reproduce the results and debug if there are errors in the code.
- Impossible to do large projects in this format

**Pros**:
- Minimal installation requirement
- Instant feedback is useful for exploration
- Can remedy the flaw by executing lines of code from a script


#### Writing script then executing them
This is the most programming coding pattern for software development.
You write your code into a script, e.g. save the following into
a file called `demo.py`.

```python
print(1 + 1)
print(1 + 2)
```

Then execute the commands by passing the script to Python for interpretation,
e.g. typing `python demo.py` into your command line in the directory where
`demo.py` is located.

Your code will be executed from top to bottom in order. Notice that the code
writing and code execution are two separate steps.

**Flaws**:
- Bugs often surface too late for beginners
- The lack of immediate feedback makes learning harder

**Pros**:
- There are simple code checkers called "linters" that check for style and
  basic syntax. These can often be installed into your editor (e.g. Pycharm).
- Most serious coding is done this way
- Most editors offer the ability to run lines of code in a REPL (and many more
  features that we won't touch on in this class).

#### Notebooks (in between REPL and scripts)
You can think of notebooks as a file with multiple "blocks", each acting
like a script. When writing code into the block, no code is executed.
One can then choose to run the code within the different blocks.

**Flaws**
- Encourages bad coding behavior like:
  - Writing long notebooks with little organization
  - The ability to run the blocks out of order often creates irreproducible 
    errors and surprises, since variables from different blocks can
    overwrite variables in each other.
- Lots of overhead to install

**Pros**
- Combines best of both REPL and script writing if done right
- The blocks allow scientific writing (e.g. LaTeX and Markdown) along with
  the code so they co-exist for better reproducibility.
- Visualizations can be seen on the notebook with the code, instead of
  saving the image to a file then viewing it in a different program.

{% include lib/mathjax.html %}
