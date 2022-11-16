import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import * as dotenv from 'dotenv'

dotenv.config();
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
      {/* SCRIPTS DEFINED IN THE REACT DOM WILL NOT RUN. need to use a workaround. read more here
      https://codingshower.com/adding-and-executing-script-tags-in-react-render/ */}
      
        {/* <script src="https://accounts.google.com/gsi/client" async defer></script>
        <script type="text/javascript">
          function handleCredentialResponse(response) {
              console.log("Encoded JWT ID token: " + response.credential);
          }
        </script> */}

        <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
