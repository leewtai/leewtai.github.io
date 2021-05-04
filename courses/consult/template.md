# Project "Searachable Tytle with Unique Spelling"

Last edited: May 4th, 2021

#### Opportunity

[Motivation for the project, potential value]

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

- Project Owner(s)
- Data Scientist(s)
- Stakeholder(s)
- Subject Matter Expert(s)

#### Requirements and metrics

[Short & long term metrics that aligns the project efforts with the project's intent. How does one know if success is achieved?]

- Deliverable
  - A documented library that ingests any video of people moving that can then
    correct identifying all the individuals then predict their emotional state.
- Coverage for test video files - 95%
- Precision controlling for recall being at least 50%
- 

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

- How will code and data be delivered?
- Who will take-over the project afterwards?
- When should hand-off begin?
- Technology requirements from the new team
- ...
