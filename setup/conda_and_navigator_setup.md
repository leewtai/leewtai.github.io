# Statistical Computing Setup

To process the data, we will use several libraries in Python or R.
To interface with these programs dynamically, for pedagogical purposes, we will leverage Jupyter Notebooks.
Finally, to manage the dependencies between Jupyter, Python, R, and the various packages, we will use Anaconda.

If our setup has potential conflicts, Anaconda will save us before it's too late!

<img src="images/conda_dep_conflict_demo.png" alt="conda dependency conflict demo" width='600'>

Overall, installing `conda` will automatically install `Python` so there are only 2 steps:
- [Install Anaconda](#install-anaconda)
- [Install jupyter notebook (and optionally R) as a package](#installing-jupyter-or-r-as-packages)

## Installing Anaconda
There are two methods to do this depending on if you're comfortable with the command line:
- Not sure: then just install [Anaconda Navigator](#anaconda-gui-via-anaconda-navigator)
- Yes, then jump ahead to [installing conda](#command-line-interface-with-anaconda-via-conda)


#### Anaconda GUI via Anaconda Navigator
1. Please get [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/) which is a nice GUI
2. Launch Anaconda Navigator
    <img src="images/anaconda_nav_home.png" alt="Anaconda Navigator Home Screen" width='400'>
3. Go to `Environments` on the left tab
4. Click on `Create` at the bottom to create a separate environment so the materials here will not conflict with your other work
    <img src="images/anaconda_nav_environments.png" alt="Anaconda Navigator Environment Tab" height='600'>
5. Create an environment called `text-mine` (or whatever you prefer) and use the dropdown menu to run under **Python version 3.7**, then choose `Create` (yes, even if you want R in the end).
    <img src="images/anaconda_nav_create_env.png" alt="Anaconda Navigator Creating New Environments" width='400'>
6. Please continue to the section on [installing packages using Anaconda Navigator](#installing-packages-using-Anaconda-Navigator)

#### Command line interface with Anaconda via conda

1. Please follow [these instructions to install miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)
2. Launch your command line interface for miniconda:
    - on Windows, this is called "Anaconda Command Prompt"
    - on OSX, this is called "Terminal"
    <img src="images/diff_command_line_prompts.png" alt="different command line prompts" width='600'>
3. Type in the following to create an environment called `text-mine` under Python version 3 (yes, even if you want R in the end!)

    `conda create -n text-mine python=3`

    You will likely be asked to confirm with the packages it'll install. Type in `y` then enter to accept.
4. Type in `conda activate text-mine` and notice how your command prompt changes to `text-mine`. It's possible
   that you have an older version of `conda`, then you should type in `source activate text-mine` instead.
      <img src="images/conda_activate_switch.png" alt="Conda activate changes prompt" width='400'>
5. Please continue to the section on [installing packages using conda](#installing-packages-using-conda)


## Installing Jupyter or R as packages under Conda
A program'ss true value is in its large community of developers and users. To leverage their work, we often will depend on packages outside of the default Python installation. Similar to before, we'll cover the instructions both using [Anaconda Navigator](#installing-packages-using-anaconda-navigator) and the [command line](#Installing-packages-using-conda).

#### Installing packages using Anaconda Navigator
1. Go back to the `Environment` tab on the far left and make sure your desired environment is selected (in this document that's `text-mine`).
    <img src="images/anaconda_nav_packages.png" alt="install packages for anaconda navigator" height='400'>
2. Use the dropdown menu shown above to examine the packages not installed.
3. Use the search box to find `jupyter`. IF you want R, you should look for `r-base`, `r-essentials`, and `r-irkernel` as well. If you are working in Python, you should look for `pandas`, `matplotlib`, `numpy`, and `statsmodels`.
    <img src="images/anaconda_nav_choosing_packages.png" alt="choosing packages in anaconda navigator" width='600'>

    I would make sure all packages you want are selected before moving to the next step. Once the ![download icon](images/download_icon.png) appears, you can safely search for the next package. Notice the number of packages selected are indicated at the right bottom of the Navigator Window.
4. (This will take awhile)  Click on `Apply` on the right bottom and wait for the packages to be installed. Click on `Apply` once more to confirm the packages you wanted.
5. To confirm it all worked, go back to the `Home` tab, make sure you use the dropdown menu behind "Applications on" to `text-mine` (or whatever you called the new environment)
    <img src="images/anaconda_nav_custom_home.png" alt="Selecting new environments" width='600'>
6. Select `Launch` under Jupyter. This should launch a few things but ultimately on your default browser, you'll see a jupyter session.
    <img src="images/jupyter_initial_launch.png" alt="Jupyter Initial Launch Screen" height='400'>
7. Click down your file path to where you want your work stored, then click on `New` on the far right to launch a `Python 3` or `R` session.
8. You should be able to confirm if the installation succeeded by repeating this little example below in your Jupyter Notebook.
    - type `1 + 1` into one of the "cells", you should see the solution appear
    - Use "Shift Enter" or "Command Enter" to run the code
        - Or you could use the "Run" button above the cells.
9. What happens if `1+1` didn't work?
    - Instead of going to the `Home` tab in step 5, stay in the `Environments` tab.
    - Click on the "Play" button in the `text-mine` tab. Choose `Python 3` or `R` then repeat the tests in step 7 and 8.


#### Installing packages using conda
1. Make sure your command line prompt activated the environment you created (`text-mine` in this document).
2. We will use the `conda install` command to install packages we need. Specifically, you should type in
    - If you are getting Python
    ```
    conda install jupyter numpy matplotlib pandas statsmodels
    ```
    <img src="images/conda_install_nltk_packages.png" alt="conda commands" width='600'>
    - If you want `R` then you should **insetad** type in:
    ```
    conda install jupyter r-base r-essentials r-irkernel
    ```
3. To confirm it all worked, navigate to your desired working directory, then type in `jupyter notebook` to launch your jupyter session. This should launch a few things but ultimately on your default browser, you'll see a jupyter session.
    <img src="images/jupyter_initial_launch.png" alt="Jupyter Initial Launch Screen" height='400'>
4. Click on `New` on the far right to launch a `Python 3` or `R` session. Now you have a functioning Jupyter notebook session
    <img src="images/initial_jupyter_session.png" alt="initial Jupyter Session" width='500'>
5. You should be able to confirm if the installation succeeded by repeating this little example below in your Jupyter Notebook
    - type `1 + 1` into one of the "cells"
    - Use "Shift Enter" or "Command Enter" to run the code
        - Or you could use the "Run" button above the cells.
