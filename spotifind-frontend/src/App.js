import React, { Fragment } from "react";
import './App.css';
import UploadImage from './components/UploadImage.js'
import LoginPage from "./components/LoginPage";


function App() {
  return (
    <Fragment> 
      <div className="container mt-2">
        <h1>Spotifind</h1>
        {/* <LoginPage/> */}
        <UploadImage/>
        <description className="container mt-2">
        <h1>
        <br></br>
      
          Spotifind turns an image into a playlist; musicify your favorite memory or any picture at all!
        </h1>
      </description>
      </div>
      

    </Fragment>

  );
}

export default App;
