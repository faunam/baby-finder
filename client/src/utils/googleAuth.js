import React from 'react';
import useScript from '../hooks/useScript'

function GoogleAuthButton() {
    useScript('https://accounts.google.com/gsi/client');

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
            <div id="g_id_onload"
            data-client_id={process.env.REACT_APP_GOOGLE_CLIENT_ID}
            // data-callback="handleCredentialResponse"
            data-login_uri="http://localhost:3000/auth/google"
            data-auto_prompt="false">
            </div>
            <div class="g_id_signin"
            data-type="standard"
            data-size="large"
            data-theme="outline"
            data-text="sign_in_with"
            data-shape="rectangular"
            data-logo_alignment="left">
            </div>
            <div id="buttonDiv"></div> 
            {/* <script>
            function handleCredentialResponse(response) {
                console.log("Encoded JWT ID token: " + response.credential)
            }
            </script> */}
            {function handleCredentialResponse(response) {
                console.log("Encoded JWT ID token: " + response.credential)
            }}

            {/* javascript method: */}
            {/* would need to use Helmet library or something to inject the below JS into the dom */}
            {/* {window.onload = () => {
                google.accounts.id.initialize({
                    client_id: process.env.REACT_APP_GOOGLE_CLIENT_ID,
                    callback: handleCredentialResponse
                });
                google.accounts.id.renderButton(
                    document.getElementById("buttonDiv"),
                    { theme: "outline", size: "large" }  // customization attributes
                );
                google.accounts.id.prompt(); // also display the One Tap dialog
            }} */} 
        </div>
    )
}

export default GoogleAuthButton;