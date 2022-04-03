import React, { Fragment } from 'react'
import { makeStyles } from '@material-ui/core/styles';
// import axios from 'axios';
// import { Button } from 'react-bootstrap'

const useStyles = makeStyles({
    login: {
        display: 'grid',
        placeItems: 'center',
        height: '10vh',

        '& a':{
          padding: '20px',
          borderRadius: '99px',
          backgroundColor: '#1db954',
          fontWeight: 600,
          color: 'white',
          textDecoration: 'none',
          position: 'absolute',
          bottom: 150,
        },

        '& a:hover':{
          backgroundColor:' white',
          borderColor: '#1db954',
          color: '#1db954',
        }
    },
});


function LoginPage() {

 const client_id = '0a96f61af1d04b7698d8bab9401a23bd';
 const redirect_uri = 'http://localhost:3000/labels';

  // const state = generateRandomString(16);
  // localStorage.setItem(stateKey, state);
  const scope = [
    'user-read-private',
    'user-read-email',
    'user-read-playback-state',
    'user-modify-playback-state',
    'streaming',
    'playlist-modify-public',
    'playlist-modify-private',
    'playlist-read-private',
    'playlist-read-collaborative',
  ].join(' ');

  let url = 'https://accounts.spotify.com/authorize';
  url += '?response_type=token';
  url += '&client_id=' + encodeURIComponent(client_id);
  url += '&scope=' + encodeURIComponent(scope);
  url += '&redirect_uri=' + encodeURIComponent(redirect_uri);
  // url += '&state=' + encodeURIComponent(state); 

  const classes = useStyles()
  return (
    <Fragment>
      <div className={classes.login}>
        <a href={url}>LOGIN WITH SPOTIFY</a>
      </div>
    </Fragment>
  )
};


export default LoginPage;
