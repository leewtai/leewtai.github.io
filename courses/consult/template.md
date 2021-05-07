# Project "Searachable Tytle with Unique Spelling"

Last edited: May 7th, 2021

#### Opportunity

[Motivation for the project, potential value and problem statement]

Communication is no longer done solely through text. With the rise of social media,
communication through emojis, gifs, video clips (e.g. TikTok) are on the rise where
traditional Natural Languages Processing (NLP) methods no longer apply.

Deep learning methods have seen a lot of sucecss in automatically extracting features
from images. Is it possible to generate a bag-of-words equivalent for video?

#### Current State

[Why is **now** a good time to start this project with some background research]

ABC et al. have collected motion tracking data from actors based on emotional prompts.
These methods do not scale to motion data recorded on video.

XYZ et al. have developed an opensource object-recognition library that can quickly
infer different moving entities within a video. Emotion was not extracted as a possible
feature within this body of work.


#### People, roles, and contacts

[The people that will approve, execute, and sustain the project]

- Project Owner(s) [Who is responsible if the project fails]
- Data Scientist(s)
- Stakeholder(s) [Who provides the resources]
- Subject Matter Expert(s) [Who understands the domain and data]

#### Requirements and metrics

[Short & long term metrics that aligns the project efforts with the project's intent.]

[Metrics include guardrail metrics vs success metrics, i.e. when do you know something is wrong vs going well?]

[Metrics should be easily calculated]

- Deliverable
  - A documented library that ingests any video of people moving that can then
    correct identifying all the individuals then predict their emotional state.
- Metrics
  - Coverage for test video files - 95% minimum
  - Precision controlling for recall being at least 50%
  - ...

#### Timeline and milestones

[Setting expectations for commitments across the group, definition of "project is kick-off ready"]

|--|--|--|
|Date|Description|People|
|4/1/2020|Kick-off & Data Delivery|John Doe, Jane Doe, and Josh Deere|
|4/7/2020|SME check-in with initial progress|John Doe, Jane Doe|
|4/15/2020|First round of results sharing|John Doe, Jane Doe, Josh Deere, Jac Deere|
|...|...|...|


#### Data Specification

[Setting expectations for commitments across the group]

|--|--|--|--|--|
|Description|Specification and attributes|Purpose|Source|Contact|
|USC Motion Tracking data|- motion data<br>- Emotional Prompt<br>- Id for individual actors<br>- ...|Required for linking motion to emotion|USC website, **approval necessary**|Expert: John Doe<br>Permissions: John Do|
|...|...|...|...|...|


#### Hand-off and maintenance

[Define project completion and potential hand-offs]

The project is complete when
  - The following R code is documented into private GitHub repository
    - Emotion prediction algorithm
    - Data ingestion, cleaning, processing
      - Automation is only required after ingestion
  - Data for the report is stored in Google Drive maintained by XYW 
  - Report for the project is reviewed and approved by ZZZ
    - If certain requirements are not satisfied by the project deadline, ...


- How will code and data be delivered?
- Who will take-over the project afterwards?
- When should hand-off begin?
- Technology requirements from the new team
- ...
