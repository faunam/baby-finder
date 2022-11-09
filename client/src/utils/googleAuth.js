import React from 'react';

function GoogleAuthButton() {

    const handleToken = (response) => {
        const responsePayload = decodeJwtResponse(response.credential);
        console.log(response);
        // const responsePayload = decodeJwtResponse(response.credential);

        // console.log("ID: " + responsePayload.sub);
        // console.log('Full Name: ' + responsePayload.name);
    }

    return (
        <div>
            <script src="https://accounts.google.com/gsi/client" async defer></script>
            <div id="g_id_onload"
                data-client_id={process.env.REACT_APP_GOOGLE_CLIENT_ID}
                data-callback="handleToken"
                data-auto_prompt="false">
            </div>
            <div className="g_id_signin"
                data-type="standard"
                data-size="large"
                data-theme="outline"
                data-text="sign_in_with"
                data-shape="rectangular"
                data-logo_alignment="left">
            </div>
            <script>
                function handleToken(response) {
                    const responsePayload = decodeJwtResponse(response.credential);

                    console.log(response)
                }
            </script>
        </div>
    )
}

export default GoogleAuthButton;