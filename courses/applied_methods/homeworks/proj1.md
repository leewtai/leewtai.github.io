# Project 1: Trustworthiness Modeling (Still in draft form)

This project is meant to see how all the different ways of modeling the same dataset can be different/similar.

We will **only focus on the 3rd study** in [Trustworthiness of crowds is gleaned in half a second](https://static1.squarespace.com/static/5daf65330e17a4220c7707ce/t/64378dd57efb4b7d3b265a54/1681362389720/ChweFreemanSPPS.pdf) by Chwe and Freeman. Make sure you read it fully!

The [original data is posted here](https://osf.io/nfgx9/) which we posted on CourseWorks.

### Task 0: Re-producing the dataset according to the description in the paper (can be time-consuming!)

- Please give a general description of the files provided by the authors.
- Please "try to reproduce" the steps that process the 3rd Study's data, starting with the files provided on CourseWorks.
  The goal here is not to be correct but to see how reproducibility can be difficult.
  - Please use comments to quote sentences from the paper that correspond to your code. Please use the format:
    ```r
    # COMMENT: "QUOTE FROM THE PAPER"
    # CODE:
    ...
    ```
- Did you discover any errors in the data?
- How would you validate the results given the copy on CourseWorks?
- Please submit this part as a separate file named `reproduce_trust.R`

Please use the 3rd study file provided on CourseWorks for the following sections.

### Reproducing the results

- For this study, how have the researchers try to convince us that the participants are representative?
- Please replicate at most 2 key results. It is part of the assignment to infer what is the most important key result from the study (there are multiple answers). How does the result get interpreted and do you agree?

### Reverse engineering

- Assume the estmated model from the paper is correct (you may need to leverage values from your reproducing efforts that are not in the paper). Simulate 500 datasets, with new users (with similar SD's) and new errors, then re-run the fitting of the model. Do the runs all share the same conclusion as the original study? Please make sure your answer includes at least one visualization to demonstrate your findings.

### Alternative models

- Use **words** to describe how are the researchers modeling the trust ratings (We will call this "model 0"), please pay close attention to the interpretation of the error term. 
- Please use visuals to justify the use for random effects at the individual level.
- Please fit the following models. If a model cannot be run, please use words to explain why you think that is the case.
  - Model 1.0: Model 0 but without any random slopes.
  - Model 1.1: Model 0 but without any random effects.
  - Model 2: Model 0 without any random effects but adding in fixed effects for demographics like age and ethnicity.
  - Model 3: Model 0 adding in random effects for the demographics like age and ethnicity.
  - Model 4: Model 0 without the independent variable of interest but only with the random effects for individuals.
  - Model 5: Model 0 but adding demographic information.
- Please compare and contrast the different models.

### Conclusion

Please write a conclusion on what you have observed and whether you believe the researchers' model is good.
