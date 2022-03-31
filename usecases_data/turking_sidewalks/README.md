# Setting up a mechanical turk for image labeling

[Amazon's mechanical turk, mturk.com](https://www.mturk.com/), is a platform to setup a mechanical turk, i.e.
crowdsourcing low-cost labor to perform tasks easy for humans
and difficult for algorithms.

This document is an updated version of the [walk-through](https://blog.mturk.com/tutorial-how-to-label-thousands-of-images-using-the-crowd-bea164ccbefc) on Amazon's
own blog describing how to **label images**.

## Overall flow
- Setup an account with AWS and mturk.com
  - AWS handles billing + storage for the images
  - mturk.com handles the coordination around the HITs
- Upload the necessary images on [AWS s3](https://s3.console.aws.amazon.com)
  - Setting the permissions on those images
- Setting up the project and HITs
- Getting the assignments from the HITs

## Key terms
- HIT: human intelligence task, the task we want crowdsourcing to perform on
- requester, the one setting up the mechanical turk
- worker, those performing the HITs.
- assignment, a submission on a particular HIT

## Setting up an account with AWS and mturk
Although both owned by Amazon, mturk.com is separate from AWS.
There is a [bug with setting up a non-root user with mturk.com](https://repost.aws/questions/QUGCubCr1LQf2GVusgTjrIHg/unable-to-log-into-my-m-turk-requester-account) so 
you need to create a root AWS account through AWS then login with
that account into mturk.com as a **requester**. Follow the [steps here](https://requester.mturk.com/signin_options) should be straight forward.

<img src="images/mturk-login.png" alt="login page for mturk.com" width='400'>


You should also create a sandbox account as a requester **AND** worker to test out your project later. This is basically a twin website for mturk.com except real workers will not access the tasks. Follow [Step 6 here](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/SetUpMturk.html) to setup your sandbox accounts. You can ignore the steps about creating access keys.


## Uploading images to s3

- The images for the workers need to be hosted on AWS s3. Login to AWS then search for the s3 console

  <img src="images/s3-search.png" alt="search for s3 on console" width='400'>
- At the landing page for s3, look for **Create Bucket**

  <img src="images/s3-landing.png" alt="landing page for s3 on console" width='400'>
- Create a bucket with the correct setup that allows public access (e.g. the workers)
  - Have a reasonable name, the public will see this in the URL. The region doesn't matter as long as it's physically close.

    <img src="images/bucket-name.png" alt="bucket name" width='400'>
  - Make sure ACL is disabled (we will use "bucket policies" to control permissions)

    <img src="images/disable-acl.png" alt="disable acl" width='400'>
  - Make sure public access is possible

    <img src="images/allow-public-access.png" alt="allow public access" width='400'>
  - The remaining default setting should be fine
- Upload files or folder to the bucket, keep all default settings
- Edit the bucket permissions under the **Permissions** tab, you should see "objects can be public"

  <img src="images/bucket-permission-tab.png" alt="allow public access" width='400'>
  - Click on `Edit` for bucket policy and look for the `Policy examples`

    <img src="images/edit-bucket-policy-view.png" alt="allow public access" width='400'>
  - Look for the section titled "[Granting read-only permission to an anonymous user](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html)"
    ```json
    {
    "Version": "2022-03-30",
    "Statement": [
        {
            "Sid": "PublicRead",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion"
            ],
            "Resource": [
                "arn:aws:s3:::DOC-EXAMPLE-BUCKET/*"
                ]
            }
        ]
    }
    ```
  - Use the policy generator to make your policy similar to the read-only example above. Your Bucket ARN should be listed under the `Policy examples` and `Policy generator` buttons. Don't forget the `/*` to indicate objects under bucket. Save these.

    <img src="images/bucket-arn.png" alt="bucket-arn" width='400'>
- Verify that you can access the images
  - You should see a warning images after saving the policy

    <img src="images/bucket-permission-overview.png" alt="verifying public access" width='400'>

  - here are ways to [access a s3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-bucket-intro.html). I recommend the "Virtual-hosted-style access"
    `https://{bucket-name}.s3.{Region}.amazonaws.com/{key-name}`
    - `{bucket-name}` in our case is `test-sidewalks`
    - `{Region}` in our case is `us-east-1`, this can be found under **Properties for your bucket** under `AWS Region`
    - `{key-name}` in our case is `streetview_-qq-zQb3RpvRXLjV0o6V1A.jpg` which can be found under **Properties for your object**. If you uploaded a folder, the folder name should precede the file name.

      <img src="images/object-properties.png" alt="object properties" width='400'>
- In addition to permissions, there's a piece of metadata, [EXIF data](https://en.wikipedia.org/wiki/Exif), that needs to be exposed, the [reasons can be found here](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/MturkCorsConfig.html).
  - Follow the instructions on [configuring cross-origin resource sharing (CORS)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enabling-cors-examples.html) for your bucket, I recommend using the s3 console then using the [example](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/MturkCorsConfig.html) like below
    ```json
    [{
      "AllowedHeaders": [],
      "AllowedMethods": ["GET"],
      "AllowedOrigins": ["*"],
      "ExposeHeaders": []
    }]
    ```
 
## Setup your project and HITs

Log back to [SANDBOX mturk.com](https://requestersandbox.mturk.com/create/projects/new), select the appropriate template under `Vision` titled `Image Classification`, then choose `Create Project`

<img src="images/mturk-template.png" alt="mturk template" width='600'>

To create the project, some advice
- Market the project somewhat

  <img src="images/edit-project1.png" alt="mturk project edit" width='600'>
- Start conservatively but allow quick feedback for adjustments

  <img src="images/edit-project2.png" alt="mturk project edit" width='600'>
- Give examples assuming the worker is not an American (e.g. driveway vs sidewalks). This should be in the instruction tab in `Design Layout`, you can embed an image there from your s3 bucket again. Here's one that is not tested but gives you an idea.
  ```html
      <crowd-image-classifier 
        src="${image_url}"
        categories="['Sidewalk is present', 'Sidewalk not present', 'Image quality too poor']"
        header="Choose the correct category"
        name="category">

       <!-- Use the short-instructions section for quick instructions that the Worker
              will see while working on the task. Including some basic examples of 
              good and bad answers here can help get good results. You can include 
              any HTML here. -->
        <short-instructions>
            <p>Is there a sidewalk where pedestrians can walk along the driving traffic?</p>
            <p>Note that private driveways and unpaved sidewalks like trails do not count.</p>
            <p>Images without a road, like farm land, would also be considered "not present"</p>
        </short-instructions>

        <!-- Use the full-instructions section for more detailed instructions that the 
              Worker can open while working on the task. Including more detailed 
              instructions and additional examples of good and bad answers here can
              help get good results. You can include any HTML here. -->
        <full-instructions header="Classification Instructions">
            <h4>Common mistakes</h4>
               <img src="https://charleston-sidewalks.s3.amazonaws.com/demo-instructions.png" alt="driveways are not sidewalks" width="400">
            <p>Choose the appropriate label that best suits the image.</p>
        </full-instructions>

    </crowd-image-classifier>
  ```
  <img src="images/demo-instructions.png" alt="image instruction" width='600'>
- You need to prepare a `input.csv` file with the s3 image urls. Recall that we set a variable called `$image_url` so the header needs to be the same, e.g.
  ```csv
  image_url
  https://charleston-sidewalks.s3.amazonaws.com/pano_images/streetview__S6cMacMuIia406jIjiT6Q.jpg
  https://charleston-sidewalks.s3.amazonaws.com/pano_images/streetview_-Hbslm-Ptx8FTLqKB1-wDQ.jpg
  https://charleston-sidewalks.s3.amazonaws.com/pano_images/streetview__uC3BQi29PRVT5uwtylv3w.jpg
  ```

