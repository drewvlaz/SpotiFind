import React from 'react';
import Spotify from "react-spotify-embed";

const ResultPage = () => {
    //filter in link from backend
    return <div>  <Spotify link="https://open.spotify.com/album/0fUy6IdLHDpGNwavIlhEsl?si=mTiITmlHQpaGkoivGTv8Jw"  
    width = "600" height = "400" frameBorder = "5000"  />
    <h1>
     Here is your playlist!!! Enjoy:)   
    </h1>
   </div>
};

export default ResultPage;
