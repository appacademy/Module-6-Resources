# AWS S3 Bucket Setup - Server Setup


In this reading we are going to acomplish the following goals:


1. Install the Boto3 package to help integrate AWS uploads in to our Flask/React applications

2. Set up necessary new `.env` variables for our AWS credentials

3. Write a helper function to make unique file names (all filenames in an S3
   bucket must be unique, a duplicate name will overwrite the existing one)

4. Write another helper function to upload files to our AWS S3 bucket, and
   ultimately return to us a public url to that saved file, to store in our
   database. (so we never change the column in our database that stores URL's as
   string, its just we now control those URL's)

5. Write yet one more helper function to handle removing files from our S3
   bucket (if a user deletes a resource attached to a file we stored, we want to
   delete the file as well)

6. Refactor our back end validations for files instead of URL strings

7. Refactor our server routes to call the helper functions as needed, and
    handle any error output to help us (and our users) debug



## Install Boto3 and Setup new ENV Variables


First use pipenv to install the `boto3` library in your project folder. Boto3
documentation is located here for a reference:
https://boto3.amazonaws.com/v1/documentation/api/latest/index.html


```shell
pipenv install boto3
```

Put the name of your bucket, along with the Access Key ID and your Secret Access
Key your `.env` file. __Make sure you include your `.env` in your `.gitignore`
as you do not want to push this information to github. (if you do by accident,
AWS will email you immediately to let you know you have expossed your
credentials, and if you don't make new ones ASAP, your account will be
suspended)

```
S3_BUCKET=<your bucket name>
S3_KEY=<Access key Id>
S3_SECRET=<Secret access key>
```


## AWS Upload


Create a file to store your AWS upload functionality, a helper file in the same
folder as your routes seems logical. You will need to import `boto3` and
`botocore` to implement your s3 functionality.  You will also have to get your
S3 credentials from your `.env`, so initially your file should look like the
following:

```python
import boto3
import botocore
import os

s3 = boto3.client(
   "s3",
   aws_access_key_id=os.environ.get("S3_KEY"),
   aws_secret_access_key=os.environ.get("S3_SECRET")
)
```

### Filenames


Your S3 bucket cannot have two files with the same filename, if you upload two
files with the same name one will get overwritten.  While we don't have any
control over the name of the file a user submits to our application, we can
change the file name once our server receives it!

We can generate unique filenames using a
[UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier), and,
specifically the biult in `uuid` module in Python.  We can also limit the types
of files users can upload in this step by setting a list of allowed file
extensions. Here is the `get_unique_filename` helper function we'll use to make
unique file names:

```python
import uuid

ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "gif"}

def get_unique_filename(filename):
    ext = filename.rsplit(".", 1)[1].lower()
    unique_filename = uuid.uuid4().hex
    return f"{unique_filename}.{ext}"
```


### Upload Helper


Now let's write the function that we'll need to actually upload the file to our
AWS S3 Bucket and return the new public URL if we're successful.

```python
BUCKET_NAME = os.environ.get("S3_BUCKET")
S3_LOCATION = f"https://{BUCKET_NAME}.s3.amazonaws.com/"

def upload_file_to_s3(file, acl="public-read"):
    try:
        s3.upload_fileobj(
            file,
            BUCKET_NAME,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )
    except Exception as e:
        # in case the our s3 upload fails
        return {"errors": str(e)}

    return {"url": f"{S3_LOCATION}{file.filename}"}
```

***When you call the `upload_file_to_s3` helper function from your route, make
sure to print the variable we are storing the return value to, as the error
messages from AWS are extremely helpful, but we won't see them if we don't print
them or return them to our front end***


We will also want to implement a similar helper function to remove files we
already uploaded to our S3 Bucket, as we don't want to store images for
resources that have been deleted.  (we can use the `upload_file_to_s3` and
`remove_file_from_s3` together to handle update functionality too!)

```python
def remove_file_from_s3(image_url):
    # AWS needs the image file name, not the URL, 
    # so we split that out of the URL
    key = image_url.rsplit("/", 1)[1]
    try:
        s3.delete_object(
        Bucket=BUCKET_NAME,
        Key=key
        )
    except Exception as e:
        return { "errors": str(e) }
    return True
```

Note when we remove a file we need the file name, not the URL, but that can be
taken from the URL with a little bit of string manipulation.

At this point, our completed AWS Helers file should look like this:

```python
import boto3
import botocore
import os
import uuid

BUCKET_NAME = os.environ.get("S3_BUCKET")
S3_LOCATION = f"https://{BUCKET_NAME}.s3.amazonaws.com/"
ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "gif"}

s3 = boto3.client(
   "s3",
   aws_access_key_id=os.environ.get("S3_KEY"),
   aws_secret_access_key=os.environ.get("S3_SECRET")
)


def get_unique_filename(filename):
    ext = filename.rsplit(".", 1)[1].lower()
    unique_filename = uuid.uuid4().hex
    return f"{unique_filename}.{ext}"


def upload_file_to_s3(file, acl="public-read"):
    try:
        s3.upload_fileobj(
            file,
            BUCKET_NAME,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )
    except Exception as e:
        # in case the our s3 upload fails
        return {"errors": str(e)}

    return {"url": f"{S3_LOCATION}{file.filename}"}


def remove_file_from_s3(image_url):
    # AWS needs the image file name, not the URL, 
    # so we split that out of the URL
    key = image_url.rsplit("/", 1)[1]
    print(key)
    try:
        s3.delete_object(
        Bucket=BUCKET_NAME,
        Key=key
        )
    except Exception as e:
        return { "errors": str(e) }
    return True
```


### WTForm Class

We can set up a form class to handle our file submissions, or we could add this
functionality to an already existing form as well.  Note that we want to import
our `FileField` input type as well as the `FileAllowed` and `FileRequired`
validators all from `flask_wtf.file`.  We can import the `ALLOWED_EXTENSIONS`
set of allowed extensions from our helpers file and provide it to the
`FileAllowed` validator like we are doing in the following code:

```python
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField
from app.routes.aws_helpers import ALLOWED_EXTENSIONS

class ImageForm(FlaskForm):
    image = FileField("Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
    submit = SubmitField("Create Post")
```

If you are using templating in your application, you will want to make a minor
change to the form in the template file, making sure you have set the encription
type on the form as follows (we now need "multipart/form-data" type since we are
sending data as well as a file):

```html
<form action="/posts/new" method="POST" enctype="multipart/form-data">
```


### On The Route


For the purposes of this tutorial, let's assume we have an Post model in our
database with a column for the image. After we've successfully uploaded the
image to S3, we can store the returned URL in our database.  The following
example is a route set up to work with `Jinja` templating, in the next reading
we will talk about refactoring to work with a `React` front end.


```python
from flask import Blueprint, request
from app.models import db, Image
from flask_login import current_user, login_required
from app.s3_helpers import (
    upload_file_to_s3, get_unique_filename)

image_routes = Blueprint("images", __name__)


@image_routes.route("", methods=["POST"])
@login_required
def upload_image():
    form = ImageForm()
 
    if form.validate_on_submit():
          
        image = form.data["image"]
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)
        print(upload)

        if "url" not in upload:
        # if the dictionary doesn't have a url key
        # it means that there was an error when we tried to upload
        # so we send back that error message (and we printed it above)
            return render_template("post_form.html", form=form, errors=[upload])

        url = upload["url"]
        new_image = Post(image= url)
        db.session.add(new_image)
        db.session.commit()
        return redirect("/posts/all")

    if form.errors:
        print(form.errors)
        return render_template("post_form.html", form=form, errors=form.errors)

    return render_template("post_form.html", form=form, errors=None)
```


At this point, our server is ready to handle file uploads to AWS, and to render
them with templating.  In the last reading we will review how to connect a React
front end form to our server to replace templates.
