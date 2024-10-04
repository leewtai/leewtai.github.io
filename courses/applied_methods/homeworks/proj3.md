# Applied Statistical Methods - Final Project

The final project is meant to encourage you to explore possible research opportunities on campus. 
It should be related to an existing research project that has a clear and relevant research question
with existing data. An ideal example would be a paper that examines a public dataset that could be
improved or a methodology that could be applied to a new domain.
A bad example would be the [diamond dataset on kaggle](https://www.kaggle.com/code/karnikakapoor/diamond-price-prediction)
 that does not solve any real problem and is purely interested in prediction.

You are encouraged to use your existing research, in another class or in your lab, for this project.

The final project in this class is open-ended with a few requirements. Key deliverables are
- A 10-15 page **written report** that contains the information below.
- An abstract written about a peer's final project, your final project can be summarized by multiple people.

### Written report
- The project must identify a research question that data can possibly falsify (10 pts)
  - Articulate the question, e.g. are there more or fewer illegal drug activities in states where neighboring states have legalized it? Or do startup founders who are minorities get asked qualitatively different questions from investors?
    - Feel free to talk to the instructor/TA if you want to identify a potential problem that's fun to you.
    - If you are improving a paper, articulate why the approach needs improving or why new fields could benefit.
  - Articulate the **ideal dataset** you would use to answer this question if money and time were not a problem. For example, all illegal activities related to drugs and the dates of the legalization of marijuana for each state.
  - Articulate why the ideal dataset and problem are related. Specifically, why the dataset would falsify one hypothesis but not another?
  - Identify an obtainable dataset that somewhat captures this information
    - Describe the data source, e.g. [Crime Data Explorer by the Gederal Bureau of Investigation](https://crime-data-explorer.fr.cloud.gov/) could be a possible data source for the criminal records.
  - Articulate the difference between this dataset and your ideal dataset, e.g. arrests do not capture all illegal activities and arrests are biased against minority neighborhoods.
  - Articulate how this dataset is still relevant to the original question.
- Examine the dataset (10 pts)
  - A summary of the data source: its time period, its coverage, its size, the notable attributes, the context around it, etc. For example, arrests per state should be reported in the context of the state populations.
  - Report any anomalies you notice in the data source.
  - The data source should come from the entity that manages the data. Management is defined by the entity that is responsible for the data quality. For example, data aggregators like Kaggle do not manage the data it posts on its challenges but Twitter manages Twitter data. Some exceptions exist like platforms like [NYC OpenData](https://opendata.cityofnewyork.us/data/) allow you to report data quality issues and will be considered a manager of the data.
  - Please describe the critical processes/decisions you made to the dataset. This should not include every possible operation but critical manipulations that could impact the outcome, e.g. aggregation, dealing with missing values, etc.
  - Create at least one graphical summary that informs you about the problem, e.g. arrest rates over time with lines that highlight the date of marijuana legalization of neighboring states. Misleading graphs that do not have a message related to the main question will receive a penalty.
- Analysis (15 pts)
  - What type of analysis would you do to make your case? e.g. do you need to fit a model to a wide enough dataset to convince investors about your superior approach?
    - Your results do not need to be conclusive!
  - What are you expect to see from the analysis? e.g. did you expect a rise or drop in arrests from your understanding of the problem? Did you have a guess on the magnitude?
  - Describe how you implemented your analysis, e.g. packages used, tuning parameters, etc
  - If applicable, are you addressing the uncertainty in your analysis?
  - Validate your model or assumptions if possible for your analysis
    - e.g. does your model fit to the data?
    - e.g. can you run a simulation that reproduces similar looking data?
- Conclusion (5 pts)
  - What was your conclusion given your original question and analysis?
    - e.g. did the results match your expectations?
    - e.g. did you have to change your question given constraints you learned in the data?
    - What else could you do?
- Code on GitHub (10pt)
  - Code (or steps) used to extract the data
  - Code used to process the data
  - Code used to create all summary statistics and graphs
  - Code used to do the analysis
  - The name of your code review partner, this will be graded on an honor code system
    - I recommend to use GitHub
  - Your code will not be examined closely but should be readable


### Abstract for a peer's project
This should be **at most** 1 paragraph that describes the question at hand, the key takeaways, and
the approach used. You should receive your peer's draft report at least a week before the
project due date to finish this task.
