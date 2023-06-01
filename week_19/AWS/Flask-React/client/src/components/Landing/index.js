import { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { setCurrentUser } from '../../store/userReducer';
import { getAllPosts } from '../../store/postReducer'
import { useHistory } from 'react-router-dom';
import './index.css';


const Landing = () => {
    const dispatch = useDispatch();
    const users = useSelector((state) => state.userState.users)
    const [selectedUser, setSelectedUser] = useState(1)
    const history = useHistory();
    
    const handleSubmit = async (e) => {
        e.preventDefault()
        dispatch(setCurrentUser(users[selectedUser]));
        await dispatch(getAllPosts(users[selectedUser]));
        history.push("/feed");
    };
    
    return(
        <div className="splash-container">
            <div>
                <h1 className="splash-title">Patchstagram</h1>
                <img className="splash-logo" 
                    src="https://res.cloudinary.com/app-academy4/image/upload/v1647291502/Patchstagram/patch_hd_riobbp.png" 
                    alt="cat-logo" 
                />
                <p className="splash-detail">The cat with so much to talk about, he needs his own social media site!</p>   
            </div>
            <div className="login-container">
                <form
                    onSubmit={ handleSubmit }
                >   
                    <div className="form-input">
                        <label 
                            className="user-label" 
                            htmlFor='user'
                        >
                            Select User:
                        </label>
                        <select
                            name='user'
                            className='user-selector'
                            onChange={e => setSelectedUser(e.target.value)}
                            value={ selectedUser }
                        >
                            {users && Object.values(users).map((user) => (
                                    <option key={ user.id } value={ user.id }>{ user.username }</option>
                                        ))
                            }
                        </select>
                    </div>
                    <button
                        type="submit"
                        className="button-link"
                    >
                        Enter
                    </button>
                </form>
            </div>
        </div>
 )};

 export default Landing;