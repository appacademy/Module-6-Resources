# AWS S3 Bucket Setup - React Setup


In this reading we are going to acomplish the following goals:


1. Refactor our front end form, as we will now need a file input field instead of a text input field

2. Refactor our front end form `onSubmit` to use `FormData` instead of making a JSON object (we need to send a file, not just data to our server, and while we can JSON stringify a file, its not an simple process.  `FormData` will allow us to send both a file and data at the same time and is much easier to implement)

3. Modify our thunk to handle sending the `FormData` instead of JSON stringifying the body.

4. Test out our AWS-S3 upload and remove functionaly

5. Celebrate integrating AWS-S3 to our application!


## Front End Form


First we will want to add `encType="multipart/form-data"` as an attribute to the form HTML tag, as we will need to use form-data and not JSON to send the request along to the server.

Next We will need to modify the input field we were using in our front end, which was probably a string field to hold a URL for the image or file you had been handling.  Now we are going to need a file input field, so we can just set the `type="file"` like in the code below.  Our onChange for the file field will also need to change, as `e.target.value` is for a string field, we are going to need `e.target.files[0]` instead, as files are stored in a different attribute, and the attribute of `files`is an array.

We can add the `accept="image/*"` attribute to the input element as well, this will gray out all files that are not images when the file folder modal opens.  Lastly, you want to remove any `value` attribute on the input field, as it will cause issues, and the file input type HTML tag does have its own built in functionality to display the name of the file you picked in the input field.  We will want our form and input tags to look like this when we are done updating the form:

``` javascript
return (
        <form 
            onSubmit={handleSubmit}
            encType="multipart/form-data"
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
```



## Refactor our Form's onSubmit Function


Next, in the same front end form component, we will want to refactor our handleSubmit to use form data instead of JSON.  Again we need to do this to send our file along with the request to the server, and we don't want to try to JSON.stringify a file.  ***(if you don't need to send a file, stick to using JSON)***

We need to create a new FormData object, and then we use the `formData.append()` method to add key value pairs of data to our FormData.  The following code implements just an image attribute, but if you have other fields on the form, just append those seperately to formData too.

```javascript
const UploadPicture = () => {
    const [image, setImage] = useState(null);
    const [imageLoading, setImageLoading] = useState(false);
    
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append("image", image);
        // aws uploads can be a bit slow—displaying
        // some sort of loading message is a good idea
        setImageLoading(true);
        await dispatch(createPost(formData));
        history.push("/images");
    }
```

***REMEMBER TO MAKE SURE YOUR KEYS IN YOUR FORMDATA ARE THE SAME AS THE KEYS YOU DEFINED IN YOUR BACK END WTFORM CLASS SO YOUR VALIDATIONS WILL WORK***


## Update Your Form's Thunk


Next we do need to make a few small changes in our thunk that handles sending the form's data to our server.  We do NOT want to set any headers for this fetch, we want to let the browser set that info for us.  We also do NOT want to `JSON.stringify()` the body of our request, because we are using formData and not JSON.  Your thunk should look similar to the code below.

```javascript
export const createImage = (post) => async (dispatch) => {
    const response = await fetch(`/images/new`, {
      method: "POST",
    //   headers: {
    //     'Accept': 'application/json',
    //     "Content-Type": "application/json",
    //   },
      body: post
    });
  
    if (response.ok) {
        const { resPost } = await response.json();
        dispatch(addPost(resPost));
    } else {
        console.log("There was an error making your post!")
    }
};
```

## Test and Celebrate!


At this point we should have everything set up and ready to test out uploading a new image from our React front end form!  Remember to print/console.log your data and errors if something isn't working.  

Below is how your component and thunk should look when you are done.

COMPONENT
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
        await dispatch(createPost(formData));
        history.push("/images");
    }
     
    return (
        <form 
            onSubmit={handleSubmit}
            encType="multipart/form-data"
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

THUNK
```javascript
export const createImage = (post) => async (dispatch) => {
    const response = await fetch(`/images/new`, {
      method: "POST",
      body: post
    });
  
    if (response.ok) {
        const { resPost } = await response.json();
        dispatch(addPost(resPost));
    } else {
        console.log("There was an error making your post!")
    }
};
```
