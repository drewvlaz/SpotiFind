import React, { Fragment,useState } from "react";
import './App.css';
import UploadImage from './components/UploadImage.js';
import LoginPage from "./components/LoginPage";
import ResultPage from "./components/ResultPage";
// import UploadImage from './components/UploadImage.js'
// import Labels from './components/Labels.js';


function App() {
  const [hidden, setHidden] = useState(true);
  return (
    <Fragment> 
      <div className="container mt-2">
        <h1>Spotifind</h1>
        {/* <LoginPage/> */}
        <UploadImage/>
      {!hidden ? <ResultPage/> : null}
      <button onClick={() => setHidden(s => !s)}>
        Playlist ready! Click here to see your playlist
      </button>
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
