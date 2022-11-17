import logo from './logo.svg';
import React, {useEffect, useState} from 'react';
import Button from '@mui/material/Button';
// import passport from 'passport';
import PhotoDisplay from './components/PhotoDisplay';
import GoogleAuthButton from './utils/googleAuth';
import { getPhotosFromApi } from './api.js';

import * as dotenv from 'dotenv'
import './App.css';

function App() {

  dotenv.config();

  const [token, setToken] = useState([]);
  const [photoData, setPhotoData] = useState({});
  const [photos, setPhotos] = useState([]);

  // const getMockPhotos = () => {
  //   fetch("/api/mock-response")
  //   .then((res) => res.json())
  //   // .then((res) => {console.log(res); return res.json()})
  //   .then((data) => {
  //     setPhotoData(JSON.parse(data));
  //     setPhotos(JSON.parse(data).photos);
  //   });
  // }

  const getPhotos = () => {
    const data = getPhotosFromApi(token.access_token)
      console.log(data);
      // setPhotoData(JSON.parse(data));
      // setPhotos(JSON.parse(data).photos);
  }

  console.log(photoData);
  
  
  return (
    <div className="App"
      >
      <div className="main"
      >
      {/* <Login></Login>
      <Logout></Logout> */}
      <div>
        {GoogleAuthButton(setToken)}
      </div>
        <Button 
            variant="contained"
            onClick={() => {
              // getMockPhotos();
              getPhotos();
            }}
          >
            Get Photos
          </Button>
        <p>
          {photos ? "Data Loaded" : "No Data" }
        </p>
        <PhotoDisplay photos={photos}></PhotoDisplay>
        {/* {photos ? PhotoDisplay({photos}) : null} */}
      </div>

    </div>
  );
}

export default App;
