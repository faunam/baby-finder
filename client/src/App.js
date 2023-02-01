import React, {useEffect, useState} from 'react';
import Button from '@mui/material/Button';
// import passport from 'passport';
import PhotoDisplay from './components/PhotoDisplay';
import GoogleAuthButton from './utils/googleAuth';
import { getPhotosFromApi, classify } from './api.js';
import { CHILD_THRESHOLD } from './constants/model';

import * as dotenv from 'dotenv'
import './App.css';

function App() {

  dotenv.config();

  const [token, setToken] = useState([]);
  const [photoData, setPhotoData] = useState({});
  const [photos, setPhotos] = useState([]);
  const [labels, setLabels] = useState([]);
  const [children, setChildren] = useState([]);
  const [nextPageToken, setNextPageToken] = useState("");

  // useEffect(() => {
  //   const filtered = labels.filter(item => {
  //     const [label, percent] = item.label;
  //     console.log(percent);
  //     return label === "child" && percent > CHILD_THRESHOLD
  //   });
  //   setChildren(children.concat(filtered));
  // }, [labels]);

  const getPhotos = async () => {
    const data = await getPhotosFromApi(token.access_token, nextPageToken);
    setPhotoData(data);
    setPhotos(data.mediaItems);
    setNextPageToken(data.nextPageToken);

    classifyPhotos(data);
  };

  const classifyPhotos = async (photos) => {
    const data = await classify(photos);
    setLabels(data);

    const filtered = data.filter(item => {
      const [label, percent] = item.label;
      console.log(percent);
      return label === "child" && percent > CHILD_THRESHOLD
    });
    setChildren(children.concat(filtered));
  };

  console.log(photoData);
  console.log('labels', labels);
  console.log('children', children);

  return (
    <div className="App"
      >
      <div className="main"
      >
        {GoogleAuthButton(setToken)}
        <Button 
            variant="contained"
            onClick={getPhotos}
            sx={{margin: "10px"}}
          >
            Get Photos
          </Button>
        <PhotoDisplay photos={photos}></PhotoDisplay>
        <PhotoDisplay photos={children}></PhotoDisplay>
      </div>

    </div>
  );
}

export default App;
