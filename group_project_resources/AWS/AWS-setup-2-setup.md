# AWS S3 Bucket Setup - Account Setup


In this reading we are going to acomplish the following goals:


1. Set up an account on AWS

2. Create a new S3 bucket for our application (to store our files)

3. Create a user to access the S3 bucket (this user has the necessary
   credentials, which if exposed we can easly create a new user with new
   credentials)


If you do not have an AWS account, you will want to make that first before you
can create a S3 bucket or a user.  You can create a new AWS account here:
https://aws.amazon.com/



## Create a New S3 Bucket


Now we will create our AWS S3 Bucket, where we will store all of our files.  If
your application is handling different types of files, like album images and mp3
song files in a music app, you might want to make a seperate S3 bucket for each
type. To start out let's navigate to
https://s3.console.aws.amazon.com/s3/home?region=us-east-1 and click on the
`Create bucket` button after you have logged in.  

On the next page, we can start by entering a name for our bucket, and then
choose a region (closest to you geographically is usually best).  Next change
the settings for ACLs to `ACLs enabled` and make sure `Bucket owner preferred`
is selected.  We are going to want to use a policy to access our bucket, so we
need to have ACLs enabled.

<img
src='https://res.cloudinary.com/app-academy4/image/upload/v1687282077/AWS/Screenshot_2023-06-20_at_1.19.10_PM_fpv688.png'
style='width: 400px;' />

In the following section we will want to set up Public File Read access on our
new AWS S3 Bucket.  Unselect the `Block all public access` check box, and you
will also need to check the acknowledge checkbox below.  Your images are going
to be accessible to the public for this demo and on your site. Be careful when
setting this for more sensitive information in the future where you do want to
block public access.

<img
src='https://res.cloudinary.com/app-academy4/image/upload/v1687282074/AWS/Screenshot_2023-06-20_at_1.22.25_PM_gfhiv5.png'
style='width: 400px;' />


We can go with the default selections for the rest of this page.  Go ahead and
click the `Create Bucket` botton on the bottom and now your bucket should be set
up!  


### Create a new User


Head to https://console.aws.amazon.com/iam/home?#/users to create a new user.  First click on the `Add users` button, and on the next page you can name the user whatever you like. Then click on the `Next` button.


On the next page, we want to select the `Attach policies directly` option.   Now we need to set up the security policy for our new user, which will detail what resources you user can access.  Unless you have previously created a policy you want to use, click the `Create policy` button, which will open up a new tab.

<img
src='https://res.cloudinary.com/app-academy4/image/upload/v1687284227/AWS/Screenshot_2023-06-20_at_2.01.32_PM_jg9tho.png'
style='width: 400px;' />


In the new tab, click the `JSON` tab/button and you should see the following:

<img
src='https://res.cloudinary.com/app-academy4/image/upload/v1687284686/AWS/Screenshot_2023-06-20_at_2.09.42_PM_vbnzqg.png'
style='width: 400px;' />


We will want to replace the default JSON policy with the below information (this is a good time to copy/paste):

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
***Make sure to replace <NAME OF BUCKET> with the name of your bucket.  We want to remove the `<` and `>` signes, but the `/*` after the bucket name does need to be there to allow access to all files added to the S3 bucket***


Click the `Next` button on the bottom to continue, and give the policy whatever name you like (e.g. s3-access-to-name-of-project). You can leave all other fields as their default, and click the `Create policy` button on the button to save the policy.  Now head back over to the other tab/window where you are creating a new user to continue the setup process.


Back in the tab where we are creating our user, we will want to refresh the `Permission policies` list (click the button next to the `Create policy` button, not the browser refresh button) and then find and select the policy we just created to attach to our user. If you don't see the policy, you can select `Customer managed` in the `Filter by Type` field, and your policy will show up. Click the `Next` button on the bottom to continue. There is no need to create tags, so you can click the `Create user` button on the bottom and now we have a user!


Almost done with the AWS account setup, our last step is we need to generate our access keys for the user we just made.  

Find the user details page, it should look like the below image, and select the `Security credentials` tab where we will want to click on the `Create access key` button.

<img
src='https://res.cloudinary.com/app-academy4/image/upload/v1687299983/AWS/Screenshot_2023-06-20_at_2.20.25_PM_fekhto.png'
style='width: 400px;' />

On the next page we want to select the setting for `Application running outside of AWS` as our sites will not be hosted on AWS.  Then click on the `Next` button to continue.

<img
src='https://res.cloudinary.com/app-academy4/image/upload/v1687300089/AWS/Screenshot_2023-06-20_at_2.20.40_PM_wenrfz.png'
style='width: 400px;' />

On this last page we can view our `Access key` and our `Secret access key`, like in the image below. You will want to keep these very safe, like in our `.env` file, and remember do not push them to github, or AWS will send you an email and suspend your account if you do not generate new credentials.

<img
src='https://res.cloudinary.com/app-academy4/image/upload/v1687300046/AWS/Screenshot_2023-06-20_at_2.20.58_PM_vmuidp.png'
style='width: 400px;' />


At this point our AWS S3 bucket and user have been created, time to start work on our server next...



