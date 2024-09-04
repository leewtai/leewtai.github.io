# Project 1: Trustworthiness Model (Still in draft form)

This project is meant to see how all the different ways of modeling the same dataset can be different/similar.

We will use the dataset from [Trustworthiness of crowds is gleaned in half a second](https://static1.squarespace.com/static/5daf65330e17a4220c7707ce/t/64378dd57efb4b7d3b265a54/1681362389720/ChweFreemanSPPS.pdf) by Chwe and Freeman. Make sure you read it fully!

The [original data is posted here](https://osf.io/nfgx9/) which we will post on CourseWorks shortly.

### Re-producing the dataset (can be time-consuming!)

The wrangling code is all written in Python. Please repeat their steps in R.
You are encouraged to use any AI technology for this step!

The raw data is stored in several separate files, here is the general description.
- `data/independent_raters/.../demo` contain the subjects' demographic information
- ...

You should name the output files `s1.csv`, `s2.csv`, and `s3.csv`.

Please submit the code in a .R file so we can run your code for validation.

### Reproducing the results

- For the **third study only**, please reproduce the overall demographic composition of the participants reported in the paper.
- Please replicate the key result (one only) from each study. It is part of the assignment to infer what is the most important key result from each study (The answer may not be unique).


### Alternative models

For this last section, focus on the 3rd study only.

- For this study, how have the researchers try to convince us that the participants are representative?
- Use **words** to describe how are the researchers modeling the trust ratings (We will call this "model 0"), please pay close attention to the interpretation of the error term. 
- Please fit the following models. If a model cannot be run, please use words to explain why you think that is the case.
  - Model 1: Model 0 but without any random effects.
  - Model 2: Model 0 without any random effects but adding in fixed effects for demographics like age and ethnicity.
  - Model 3: Model 0 adding in random effects for the demographics like age and ethnicity.
  - Model 4: Model 0 without the independent variable of interest but only with the random effects for individuals.
  - Model 5: Your best attempt at modeling the trust ratings data. 
- Please compare and contrast the different models.

### Conclusion

Please write a conclusion on what you have observed and whether you believe the researchers' model is ideal.
