# AWS S3 Bucket Setup - Setup

IN this reading we are going to acomplish the following goals:

1. Set up an account on AWS

2. Create a new S3 bucket for our application (to store our files)

3. Create a user to access the S3 bucket (this user has the necessary
   credentials, which if exposed we can easly create a new user with new
   credentials)


If you do not have an AWS account, you will want to make that first before you can create a S3 bucket or a user.  You can create a new AWS account here: https://aws.amazon.com/


## Create a New S3 Bucket


Navigate to https://s3.console.aws.amazon.com/s3/home?region=us-east-1 click on
“create bucket”, enter a name for your bucket, and then choose a region.

Next we will want to set up Public File Read access on our new AWS S3 Bucket.
Unblock all public access. Your images are going to be accessible to the public
for this demo. Be careful when setting this for more sensitive information in
the future where you do want to block public access.

<img
src='https://github.com/jamesurobertson/aws-s3-pern-demo/blob/master/assets/block-public-access.png' style='width: 400px;' />

Change the settings to ACLs Enabled and Bucket owner preferred.

<img
src='https://user-images.githubusercontent.com/89059894/168724412-e4c330de-bbc7-4729-b6a4-da18133a6de3.png'
style='width: 400px;' />

Hit Save Changes and your bucket should be all set up!  


### Create a new User


Head to https://console.aws.amazon.com/iam/home?#/users to create a new user.
Name the user whatever you like. Give the user Programmatic access. Proceed to
the next step. Now you need to set up the security policy for your new user.
This is how they will be allowed to connect. Click 'Attach existing policies
directly' and then 'Create Policy'. This will open up a new tab.

In the new tab, click the JSON tab and paste the following:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1420751757000",
      "Effect": "Allow",
      "Action": ["s3:*"],
      "Resource": "arn:aws:s3:::<NAME OF BUCKET>/*"
    }
  ]
}
```
***Make sure to replace <NAME OF BUCKET> with the name of your bucket. Click
Review Policy.***

Give the policy whatever name you like (e.g. s3-access-to-name-of-project).
After you save and create the policy, head back over to the other tab/window
where you are creating a new user.

Click the refresh button all the way to the right of the Create Policy button
then search for the policy that you just created. Check that policy then head
over to the next step. You can skip additional tags. Create the user.

After you create the user, you will get the Access Key ID and the Secret Access
Key.   You will want to keep these very safe.
