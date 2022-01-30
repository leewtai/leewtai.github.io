# Visualization in Python

There are 2 main packages you need to familiarize yourself to make
decent Python graphics:
- `matplotlib.pyplot` often shortened as `plt` in code
- `seaborn` often shortened as `sns` in code

Overall, `seaborn` creates modern looking visuals but `matplotlib.pyplot`
controls some important internals between graphics. For example,
plotting 2 subplots side by side requires `plt` to coordinate the
two plots but `sns` will create beautiful looking plots without
much specification.

The [`seaborn` tutorial](https://seaborn.pydata.org/tutorial.html)
is quite thorough. I recommend reading the "Data structures accepted by seaborn"
before reading the "Overview of seaborn plotting functions".

To examine the plots:
- if you want to do so interactively, then you need to call `plt.show()` at
  the end of your code. This often launches a separate program that will
  show the graphic. This will hold-up your REPL session until you close the
  program (i.e. you cannot type in new commands to the REPL) so be careful.
- if you want to save the plots, then I recommend `plt.savefig('MYPLOTNAME.png')`.
  This will save it to the current working directory and allow you to revisit
  this later. This function will overwrite any plot that shares the same name,
  without warning, so be careful as well.
- It is good practice to call `plt.close()` at the end of each plot to ensure
  you do not send data from one graphic to another by accident.


The example below is a simplified version from the [seaborn tutorial on
function overview](https://seaborn.pydata.org/tutorial/function_overview.html)
to show all the commands in one code block. I recommend you to add the
additional parameters back into the example below to 

```python
import matplotlib.pyplot as plt
import seaborn as sns

penguins = sns.load_dataset("penguins")

f, axs = plt.subplots(1, 2)  # 1 row and 2 columns for the subplots
sns.scatterplot(data=penguins,
                x="flipper_length_mm",
                y="bill_length_mm",
                hue="species",
                ax=axs[0]) # This places this graph on the first subplot
sns.histplot(data=penguins,
             x="species",
             hue="species",
             legend=False, # This is supresses bc the first subplot has it
             ax=axs[1])    # This places this graph on the second subplot
plt.savefig('test_seaborn.png') # create a file at your working directory
plt.close()
```

To create good graphics, most people think about what they want to plot,
look up examples online that shows a similar graphic, then tweaks the
code until they achieve the desired graphic.
