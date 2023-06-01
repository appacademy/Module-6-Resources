import { normalizeObj } from "./helpers";

const GET_USERS = 'users/GET_USERS';
const SET_CURRENT = 'users/SET_CURRENT';

// ACTIONS
export const getUsers = (users) => {
    return {
        type: GET_USERS,
        users
    };
};

export const setCurrentUser = (currentUser) => {
    return {
        type: SET_CURRENT,
        currentUser
    }
};


// THUNKS
export const getAllUsers = () => async (dispatch) => {
    const response = await fetch("/users/all")
    if(response.ok){
        const { users } = await response.json();
        dispatch(getUsers(users))
    } else {
        console.log("There was an error getting all users!")
    }
};


const initialState = {};

const userReducer = (state = initialState, action) => {
    let newState;
    switch (action.type) {
        case GET_USERS:
            newState = { ...state };
            newState.users = normalizeObj(action.users);
            return newState
        case SET_CURRENT:
            newState = { ...state }
            newState.currentUser = action.currentUser;
            return newState 
        default:
            return state;
  }
};

export default userReducer;