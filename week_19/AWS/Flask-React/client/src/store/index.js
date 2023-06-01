import { createStore, applyMiddleware, compose, combineReducers } from 'redux';
import thunk from 'redux-thunk';
import postReducer from './postReducer';
import userReducer from './userReducer';
/* combineReducers turns all the reducer functions into one big reducer function
 */
/* this is the most important part of this file. you will add your reducers here
to work with your components. you are creating one big reducer */
const rootReducer = combineReducers({
    userState: userReducer,
    postState: postReducer
});

let enhancer;

/* enhancer allows you to alter the store and add functionality such as redux
 devtools, logger (similar to morgan) middleware */

/* compose gives you the ability to add more than one enhancer to the store */
/* env comes automatically in create-react-app */
/* process.env.NODE_ENV has 3 settings:
   1. running npm start makes process.env.NODE_ENV ='development`
   2. running npm test makes process.env.NODE_ENV = 'test'
   3. running npm run build makes process.env.NODE_ENV = 'production' which you
      will use with heroku
*/
/* window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__({ trace: true }) along with the
chrome extension for redux devtools will set up your Redux DevTools in the
browser */
if (process.env.NODE_ENV !== 'production') {
  const logger = require('redux-logger').default;
  const composeEnhancers =
    typeof window === 'object' && window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__
      ? window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__({ trace: true })
      : compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

/* createStore creates a store object literal {} */
/* preloaded state, not important for now, mainly used for hydrating state from
the server */
/* enhancer see above */

/*this is the variable you will use in your root index.js to give Redux store
access to the full application */
const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;