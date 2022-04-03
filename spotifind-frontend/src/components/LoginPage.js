import React, { useEffect, Fragment } from 'react'
import axios from 'axios';
import { makeStyles } from '@material-ui/core/styles';

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
 const redirect_uri = 'http://localhost:3000/callback';

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
  ].join(' ');

  let url = 'https://accounts.spotify.com/authorize';
  url += '?response_type=token';
  url += '&client_id=' + encodeURIComponent(client_id);
  url += '&scope=' + encodeURIComponent(scope);
  url += '&redirect_uri=' + encodeURIComponent(redirect_uri);
  // url += '&state=' + encodeURIComponent(state); 
  //

  useEffect(() => {
    // const authToken = window.location.hash.split("=")[1].split("&")[0];
    const authToken = "alsdfjlksajfdlsalf";
    console.log(authToken);
    const payload = { authToken: authToken }
    const sendAuthToken = async (payload) => {
      await axios
      .post("http://localhost:5000/flask/hello", payload)
      .then((res) => console.log(res));
    }
    sendAuthToken(payload);
  }, []);

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
