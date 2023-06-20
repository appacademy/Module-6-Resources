# AWS S3 Bucket Setup - Intro



## Why do we want to integrate a AWS S3 bucket in to our Applications?



When we visit a professional website, and we are asked to provide an image (or
music or video), we are asked to provide a file, not a url.  This is for a few
reasons, first not every user has the ability to host their files and provide
urls, but also an external url that your application does not have any control
over can easily be changed, and then your site is the one with a broken image
link.

Why don't we just use our database you ask?  Database are great for storing
data, but mostly in string formats, not significantly larger files like images,
songs, and videos. (While a database CAN store files, it will hurt our query
performance as the files add more data to search through)  We are still going to
store urls for our files we upload in our database as strings (so really
implementing AWS S3 bucket uploading is really similar to `middleware`) but the
actual data for those files will be stored on AWS.  



## General overview of the AWS-S3 upload process

We are going to assume in this walkthrough that you already have a functional
form/route for handling new resources that currently accepts and stores URL's as
strings, but we want to refactor to accept files instead.  Here is a very high
level overview of what we are looking to accomplish to interate file uploads:

1. Set up an account on AWS

2. Create a new S3 bucket for our application (to store our files)

3. Create a user to access the S3 bucket (this user has the necessary
   credentials, which if exposed we can easly create a new user with new
   credentials)

4. Install the Boto3 package to help integrate AWS uploads in to our Flask/React
   applications

5. Set up necessary new `.env` variables for our AWS credentials

6. Write a helper function to make unique file names (all filenames in an S3
   bucket must be unique, a duplicate name will overwrite the existing one)

7. Write another helper function to upload files to our AWS S3 bucket, and
   ultimately return to us a public url to that saved file, to store in our
   database. (so we never change the column in our database that stores URL's as
   string, its just we now control those URL's)

8. Write yet one more helper function to handle removing files from our S3
   bucket (if a user deletes a resource attached to a file we stored, we want to
   delete the file as well)

9. Refactor our back end validations for files instead of URL strings

10. Refactor our server routes to call the helper functions as needed, and
    handle any error output to help us (and our users) debug





11. Refactor our front end form, as we will now need a file input field instead
    of a text input field

12. Refactor our front end `onSubmit` to use `FormData` instead of making a JSON
    object (we need to send a file, not just data to our server, and while we
    can JSON stringify a file, its not an simple process.  `FormData` will allow
    us to send both a file and data at the same time and is much easier to
    implement)

13. Modify our thunk to handle sending the `FormData` instead of JSON
    stringifying the body.

14. Test out our AWS-S3 upload and remove functionaly

15. Celebrate integrating AWS-S3 to our application!

