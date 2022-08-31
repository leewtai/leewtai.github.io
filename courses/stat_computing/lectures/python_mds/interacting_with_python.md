# Interacting with Python

Basic programming is about writing instructions for the computer to execute
tasks like reading in some data. Here we will write these instructions in
Python. Before you can assign instructions though, there are some key things
to know first.

## Some basics about folder structure
You need to know the "location" of
- Where is your data
- Where to invoke Python
- Where is your "working directory", i.e. where Python assumes 

All files (data or programs) are organized by folders (e.g. Downloads
vs Documents vs Desktop) on modern operating
systems (e.g. MacOS and Windows). Most beginners encounter problems
with instructions like "read in this file" because Python has a different
understanding of where "this data" is referring to. The folder where
Python assumes you're working from is called the "working directory".

Another important topic is "permissions" related to these files if
you are encountering further problems. Ask a TA or Google online to
learn more about permissions.

## The different modes of working with Python
Python enables one to issue instructions to the
computer, these are often referred to as "commands".
You'll write instructions called code, that Python can
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
You can directly type code into the REPL, i.e. the space after `>>>`.

<img src="images/command_line.png" alt="REPL demo" width='600'>

**Flaws**:
- The commands in the REPL are not saved to a file so it is hard
  to reproduce the results and debug if there are errors in the code.
- __Impossible__ to do projects in this format

**Pros**:
- Minimal installation requirement
- Instant feedback is useful for exploration
- Can remedy the flaw by executing lines of code from a script


#### Writing script then executing them
This is the most common coding pattern for software development (not true
for data analysis). You write your code into a script, e.g. save the following into
a file called `demo.py` then execute the commands by passing the script to
Python for interpretation,
e.g. typing `python demo.py` into your command line in the directory where
`demo.py` is located.


```python
# demo.py

print(1 + 1)
print(1 + 2)
```

Your code will be executed from top to bottom in order. Notice that the code
writing and code execution are two separate steps.

**Flaws**:
- Bugs often surface too late for beginners
- The lack of immediate feedback makes learning harder

**Pros**:
- There are simple code checkers called "linters" that check for style and
  basic syntax. These can often be installed into your editor (e.g. PyCharm).
- Most serious coding is done this way
- Most editors offer the ability to run lines of code in a REPL (and many more
  features that we won't touch on in this class).

#### Notebooks (in between REPL and scripts)
Notebooks allow you to write "blocks" of code as in a script without executing them,
then you can choose to run the code in different blocks individually or together.

**Flaws**
- Encourages bad coding behavior like:
  - Writing long notebooks with little organization
  - People often run the blocks out of order which creates irreproducible 
    errors and surprises. It's best practice to re-run all your analysis sequentially
    to double check your findings.
- More overhead to install

**Pros**
- Combines best of both REPL and script writing if done right
- The blocks allow scientific writing (e.g. LaTeX and Markdown) with equations to
  co-exist with the code for better reproducibility.
- Visualizations can be seen on the notebook with the code, instead of
  saving the image to a file then viewing it in a different program.
- This is the most user-friendly for beginners once you've installed it properly.

{% include lib/mathjax.html %}
