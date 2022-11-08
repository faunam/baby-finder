import logo from './logo.svg';
import React, {useEffect, useState} from 'react';
import Button from '@mui/material/Button';
// import passport from 'passport';
import PhotoDisplay from './components/PhotoDisplay';
import {auth} from './auth.js';
import './App.css';

function App() {

  const [data, setData] = useState();
  const [photoData, setPhotoData] = useState({});
  const [photos, setPhotos] = useState([]);

  // auth(passport);

  // passport.initialize();
  // passport.session();

  // useEffect(() => {
  //   // doesnt seem like the best way to do this, probably more async savy way.
  //   fetch("/api")
  //     .then((res) => res.json()) // why not do this and following in same step? promise thing?
  //     .then((data) => setData(data.message));
  // }, []);

  const getHello = () => {
    setData('Loading');
    
    fetch("/api/calculate")
    .then((res) => res.json())
    .then((data) => setData(data.message));
  }

  const getMockPhotos = () => {
    fetch("/api/mock-response")
    .then((res) => res.json())
    // .then((res) => {console.log(res); return res.json()})
    .then((data) => {
      setPhotoData(JSON.parse(data));
      setPhotos(JSON.parse(data).photos);
    });
  }

  const googleLogin = () => {
    
    // passport.authenticate('google', {
    //   scope: config.scopes,
    //   failureFlash: true,  // Display errors to the user.
    //   session: true,
    // });
  }

  return (
    <div className="App"
      >
      <div className="main"
      >
        <Button 
          variant="contained"
          onClick={() => {
            getMockPhotos();
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
