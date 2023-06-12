




11. Refactor our front end form, as we will now need a file input field instead of a text input field

12. Refactor our front end `onSubmit` to use `FormData` instead of making a JSON object (we need to send a file, not just data to our server, and while we can JSON stringify a file, its not an simple process.  `FormData` will allow us to send both a file and data at the same time and is much easier to implement)

13. Modify our thunk to handle sending the `FormData` instead of JSON stringifying the body.

14. Test out our AWS-S3 upload and remove functionaly

15. Celebrate integrating AWS-S3 to our application!












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
