import { useEffect } from 'react';
import { useDispatch } from "react-redux";
import { Switch, Route } from 'react-router-dom';
import { getAllUsers } from './store/userReducer';
import './App.css';
import Landing from './components/Landing';
import Navbar from './components/Navbar';
import Feed from "./components/Feed";
import Footer from './components/Footer';
import PostForm from './components/PostForm';


const App = () => {
  const dispatch = useDispatch();

  
  useEffect(() => {
    (async () => {
      await dispatch(getAllUsers());
    })();
  }, [dispatch]);
  
  return (
    <div className="App">
      <Switch>
        <Route exact path="/">
          <Landing />
          <Footer />
        </Route>
        <Route path="/feed">
          <Navbar />
          <Feed />
        </Route>
        <Route path="/newpost">
          <Navbar />
          <PostForm />
        </Route>s
      </Switch>
      
    </div>
  );
}

export default App;
