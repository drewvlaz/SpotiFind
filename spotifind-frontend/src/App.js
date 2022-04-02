import React, { Fragment } from "react";
import './App.css';
import Labels from './components/Labels.js';

function App() {
  return (
    <Fragment> 
      <div className="container mt-2">
        <h1>SpotiFind</h1>
      </div>
      <Labels />
    </Fragment>
  );
}

export default App;
