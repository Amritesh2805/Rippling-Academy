import "bootswatch/dist/lux/bootstrap.min.css"
import './App.css';
import React from 'react'
import Header from './components/Header';
import Home from "./screens/Home";
import Notes from "./screens/Notes";
import Create from "./screens/Create";
import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom"; 


function App() {
  return (
    <div>
      <Header/>
      <Switch>
      <Route exact path='/home'><Home/></Route>
      <Route path='/notes'><Notes/></Route>
      <Route path='/create'><Create/></Route>
      </Switch>
    </div>
  );
}

export default App;
