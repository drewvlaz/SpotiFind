import React, { Fragment } from "react";
import './App.css';
import UploadImage from './components/UploadImage.js'
import LoginPage from './components/LoginPage.js';
// import Labels from './components/Labels.js';


function App() {
  // const hash = window.location.hash.split("=")[1].split("&")[0];
  // console.log(hash);
  return (
    <Fragment> 
      <div className="container mt-2">
        <h1>SpotiFind</h1>
        <div className="container mt-4">
          <p1>
            SpotiFind turns an image into a playlist; musicify your favorite memory or any picture at all!
          </p1>
        </div>
        <div className="container mt-4">
          <LoginPage/>
        </div>
      </div>
    </Fragment>

  );
}

export default App;
