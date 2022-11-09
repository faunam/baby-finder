import React from 'react';
import google from 'googleapis';

function GoogleAuthButton() {

    const handleToken = (response) => {
        console.log(response);
        // const responsePayload = decodeJwtResponse(response.credential);

        // console.log("ID: " + responsePayload.sub);
        // console.log('Full Name: ' + responsePayload.name);
    }

    const handleCredentialResponse = (response) => {
        console.log("Encoded JWT ID token: " + response.credential);
    }


    return (
        <div>
            <script src="https://accounts.google.com/gsi/client" async defer></script>
            <div id="buttonDiv"></div> 
            {window.onload = () => {
                google.accounts.id.initialize({
                    client_id: process.env.REACT_APP_GOOGLE_CLIENT_ID,
                    callback: handleCredentialResponse
                });
                google.accounts.id.renderButton(
                    document.getElementById("buttonDiv"),
                    { theme: "outline", size: "large" }  // customization attributes
                );
                google.accounts.id.prompt(); // also display the One Tap dialog
            }}
        </div>
    )
}

export default GoogleAuthButton;