import React from 'react'
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
        },

        '& a:hover':{
            backgroundColor:' white',
            borderColor: '#1db954',
            color: '#1db954',
        }
    },
});


function LoginPage() {
    const classes = useStyles()
    return (
        <div className="container mt-4">
        <div className={classes.login}>
            <a href="#">LOGIN WITH SPOTIFY</a>
        </div> 
        </div> 
    )}
    

export default LoginPage;
