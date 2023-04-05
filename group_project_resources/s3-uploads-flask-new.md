# Using S3 for image upload with Flask


## Create your AWS User and Bucket


Here we will set up a new S3 bucket, and a new users on the same account to
access that S3 bucket.  If you do not have an AWS account, you will want to make
that first before you can create a S3 bucket or a user.  You can create a new
AWS account here:  https://aws.amazon.com/


### Create a new Bucket


Navigate to https://s3.console.aws.amazon.com/s3/home?region=us-east-1 click on
“create bucket”, enter a name for your bucket, and then choose a region.

Next we will want to set up Public File Read access on our new AWS S3 Bucket.
Unblock all public access. Your images are going to be accessible to the public
for this demo. Be careful when setting this for more sensitive information in
the future where you do want to block public access.

<img
src='https://github.com/jamesurobertson/aws-s3-pern-demo/blob/master/assets/block-public-access.png'/>

Change the settings to ACLs Enabled and Bucket owner preferred.

<img
src='https://user-images.githubusercontent.com/89059894/168724412-e4c330de-bbc7-4729-b6a4-da18133a6de3.png'/>

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



## Install Boto3 and Setup new ENV Variables


First use pipenv to install the `boto3` library in your project folder. Boto3
documentation is located here for a reference:
https://boto3.amazonaws.com/v1/documentation/api/latest/index.html


```shell
pipenv install boto3
```

Put the name of your bucket, along with the Access Key ID and your Secret Access
Key your `.env` file. __Make sure you include your `.env` in your
`.gitignore`__. You really don't want to push this information to github.

```
S3_BUCKET=<your bucket name>
S3_KEY=<Access key Id>
S3_SECRET=<Secret access key>
```

## AWS Upload


Create a file for AWS upload functionality. You will need to import `boto3` and
`botocore` to implement your s3 functionality. You will also have to get your S3
values from the environment

```python=
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

Your S3 bucket cannot have two files with the same filename—if you upload two
files with the same name one will get overwritten. We can avoid issue that by
generating unique names every time we upload a file.

We can generate unique filenames using a
[UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier), and,
specifically the `uuid` module in Python. We can also limit the types of files
users can upload in this step.

Here are the helper functions we'll use to get filenames.

```python=
import uuid

ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "gif"}

def get_unique_filename(filename):
    ext = filename.rsplit(".", 1)[1].lower()
    unique_filename = uuid.uuid4().hex
    return f"{unique_filename}.{ext}"
```

### Upload Helper

Now let's write the function that we'll need to actually upload the file—and
return the url if we're successful.

```python
BUCKET_NAME = os.environ.get("S3_BUCKET")
S3_LOCATION = f"http://{BUCKET_NAME}.s3.amazonaws.com/"

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

So, at this point, our file looks like this:

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
`FileAllowed` validator.


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
type on the form as follows:

```html
<form action="/posts/new" method="POST" enctype="multipart/form-data">
```


### On The Route

For the purposes of this tutorial, let's assume we have an Post model in our
database with a column for the image. After we've successfully uploaded the
image to S3, we can store the returned URL in our database.  The following
example is a route set up to work with `Jinja` templating, later in this reading
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

        if "url" not in upload:
        # if the dictionary doesn't have a url key
        # it means that there was an error when we tried to upload
        # so we send back that error message
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



## Sending images from the frontend


Here is a simple example of a component for users to upload images. You will
undoubtedly need to modify this for your usage, but make sure that the name of
the field you attach to your `FormData` object matches what you are looking for
on the backend end (i.e. the name in `formData.append("<some name>", image);`
should match `image = request.files["<some name>"]`).

Note that you must NOT set the `Content-Type` header on your request. If you
leave the `Content-Type` field blank,  the `Content-Type` will be generated and
set correctly by your browser (check it out in the network tab!). If you include
`Content-Type`, your request will be missing information and your Flask backend
will be unable to locate the attached files.  You will also want to set the
encryption type to "multipart/form-data" like you did on the template form
above. (in `React` we would do that with `encType="multipart/form-data"`)


```javascript
import React, {useState} from "react";
import { useHistory } from "react-router-dom";


const UploadPicture = () => {
    const history = useHistory(); // so that we can redirect after the image upload is successful
    const [image, setImage] = useState(null);
    const [imageLoading, setImageLoading] = useState(false);
    
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append("image", image);
        
        // aws uploads can be a bit slow—displaying
        // some sort of loading message is a good idea
        setImageLoading(true);

        const res = await fetch('/api/images', {
            method: "POST",
            body: formData,
        });
        if (res.ok) {
            await res.json();
            setImageLoading(false);
            history.push("/images");
        }
        else {
            setImageLoading(false);
            // a real app would probably use more advanced
            // error handling
            console.log("error");
        }
    }
     
    return (
        <form 
            onSubmit={handleSubmit}
            encType="multipart/form-data")
        >
            <input
              type="file"
              accept="image/*"
              onChange={(e) => setImage(e.target.files[0])}
            />
            <button type="submit">Submit</button>
            {(imageLoading)&& <p>Loading...</p>}
        </form>
    )
}

export default UploadPicture;
```

## Working Demo
 - Check out [this repo](https://github.com/jshafto/widget_app) to see this code
   in context.



## Credits
 - Boto3 Docs [boto3
   docs](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
 - Flask_wtf docs [flask_wtf docs on file
   uploads](https://flask-wtf.readthedocs.io/en/1.0.x/form/?highlight=file#file-uploads)
 - AWS setup walkthrough for Express [aws-s3 tutorial on
   express](https://github.com/jamesurobertson/aws-s3-pern-demo)
