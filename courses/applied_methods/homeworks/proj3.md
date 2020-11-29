# Open ended project

The final project in this class is open-ended with a few requirements. Key deliverables are
- A 5-15 page **written report** that contains the information below.
- A **30min oral defense** regarding this written report with the instructor during finals week.
- An abstract written about a peer's final project, your final project can be summarized by multiple people.
- (optional) A code review for your peer's code

### Written report
- The project must identify a question that data can possibly falsify or support (10 pts)
  - Articulate the question, e.g. are there more or fewer illegal drug activities in the states where marijuana is still illegal but their neighboring states has legalized it? Or a StartUp idea such as can I classify instagram food images better than Google's default image classifier?
    - Feel free to talk to the instructor/TA if you want to identify a potential problem that's fun to you.
  - Articulate the **ideal dataset** you would use to answer this question if money and time were not a problem. For example, all illegal activities related to drugs and the dates of the legalization of marijuana for each state.
  - Articulate why the dataset and problem are related.
  - Identify an obtainable dataset that captures this information
    - Describe the data source, e.g. [Crime Data Explorer by the Gederal Bureau of Investigation](https://crime-data-explorer.fr.cloud.gov/) could be a possible data source for the criminal records.
  - Articulate the difference between this dataset and your ideal dataset, e.g. arrests do not capture illegal activities and arrests are biased against minority neighborhoods.
  - Articulate how this dataset is still relevant to the original question.
- Examine the dataset (10 pts)
  - A summary of the data source: its time period, its coverage, its size, the notable attributes, the context around it, etc. For example, arrests per state should be reported in the context of the state populations.
  - Report any anomalies you notice in the data source.
  - The data source should come from the entity that manages the data. Management is defined by the entity responsible if the data has quality issues. For example, data aggregators like Kaggle do not manage the data it posts on its challenges but Twitter manages Twitter data. Some exceptions exist like platforms like [NYC OpenData](https://opendata.cityofnewyork.us/data/) allow you to report data quality issues and will be considered a manager of the data.
  - Please describe the critical processing steps you did to the dataset. This should not include every possible operation but critical manipulations that could impact the outcome, e.g. aggregation, dealing with missing values, etc.
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


### Oral Defense
Closer to the finals week a scheduling sheet will be posted for you to sign up for 30 minute
slots.

You will be asked to summarize your project in your own words as if this were an interview.
This should be around 2-3 minutes.

You will need to answer questions regarding your project. The questions will be related
to the course content. The key is to be honest and correct. Treat this like an interview.


### Abstract for a peer's project
This should be **at most** 1 paragraph that describes the question at hand, the key takeaways, and
the approach used. You should receive your peer's draft report at least a week before the
project due date to finish this task.
