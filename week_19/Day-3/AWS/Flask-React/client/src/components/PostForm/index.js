import { useSelector, useDispatch } from 'react-redux';
import { useState, useEffect } from 'react';
import { createPost } from '../../store/postReducer';
import { useHistory } from 'react-router-dom';
import './index.css';


const PostForm = () => {
    // form state
    const [caption, setCaption] = useState('');
    const [image, setImage] = useState('');
    const [validationErrors, setValidationErrors] = useState([]);
    const [hasSubmitted, setHasSubmitted] = useState(false);
    // current user state
    const currentUser = useSelector((state) => state.userState.currentUser);
    const dispatch = useDispatch();
    const history = useHistory();

  
    const submitForm = async (e) => {
        e.preventDefault();

        setHasSubmitted(true);
        if (validationErrors.length) return alert("Your Post has errors, cannot submit!");
        
        // const newPost = {
        //     caption,
        //     author: currentUser.id,
        //     image,
        // };


        const formData = new FormData()
        formData.append("caption", caption)
        formData.append("image", image)
        formData.append("author", currentUser.id)

        
        await dispatch(createPost(formData));

        setCaption('');
        setImage('');
        setValidationErrors([]);
        setHasSubmitted(false);
        history.push("/feed");
    }

    useEffect(() => {
        const errors = [];
        if (!caption.length) errors.push("Please enter a post caption!");
        if (!image) errors.push("Please provide an image!");
        setValidationErrors(errors);
    }, [caption, image])

 
    return (
        <div className="form-page">
            <div className="form-container">
                <h1 className="form-header"> Create New Post</h1>
                {hasSubmitted && validationErrors.length > 0 && (
                    <div className="errors-info">
                        <h2>The following errors were found:</h2>
                        <ul>
                            {validationErrors.map(error => (
                            <li key={error}>{error}</li>
                            ))}
                        </ul>
                    </div>
                )}
                <form onSubmit={(e) => submitForm(e)} encType="multipart/form-data">
                    <h3 className="form-label">User: { currentUser.username }</h3>
                    <div className='form-input-box'>
                        <label 
                            className="form-label" 
                            htmlFor='caption'
                        >
                            Post Caption:
                        </label>
                        <input
                            id="caption"
                            type="text"
                            onChange={(e) => setCaption(e.target.value)}
                            value={caption}
                            >
                        </input>
                    </div>
                    <div className='form-input-box'>
                        <label 
                            className="form-label" 
                            htmlFor='image'
                        >
                            Post Image:
                        </label>
                        <input
                            id="image"
                            type="file"
                            accept="image/*"
                            onChange={(e) => setImage(e.target.files[0])}
                            >
                        </input>
                    </div>
                    <button className="button">Submit</button>
                </form>
            </div>
        </div>
)};

export default PostForm;