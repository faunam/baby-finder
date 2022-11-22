import React, { useEffect } from 'react';
import GoogleLogin from 'react-google-login';
import { gapi } from 'gapi-script';

const GoogleAuthButton = (setToken) => {

    useEffect(() => {
        const initClient = () => {
              gapi.client.init({
              clientId: process.env.REACT_APP_GOOGLE_CLIENT_ID,
              // scope: space delimited string
              scope: 'https://www.googleapis.com/auth/photoslibrary.readonly profile',
            });
         };
         gapi.load('client:auth2', initClient);
     });

    const handleFailure = (result) => {
        console.log(result);
    }

    const handleLogin = (googleData) => {
        console.log(googleData);
        setToken(googleData.tokenObj);
    }


    return (
        <div>
            <GoogleLogin
                clientId={process.env.REACT_APP_GOOGLE_CLIENT_ID}      
                buttonText="Log in with Google"
                onSuccess={handleLogin}
                onFailure={handleFailure}
                cookiePolicy={'single_host_origin'}
                isSignedIn={true} // maybe take out
            ></GoogleLogin>
        </div>
    )
}

export default GoogleAuthButton;