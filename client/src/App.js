import logo from './logo.svg';
import React, {useEffect, useState} from 'react';
import Button from '@mui/material/Button';
// import passport from 'passport';
import PhotoDisplay from './components/PhotoDisplay';
import GoogleAuthButton from './utils/googleAuth';
import { getPhotosFromApi, modelTest, sendSampleData} from './api.js';

import * as dotenv from 'dotenv'
import './App.css';

function App() {

  dotenv.config();

  const [token, setToken] = useState([]);
  const [photoData, setPhotoData] = useState({});
  const [photos, setPhotos] = useState([]);
  const [classified, setClassified] = useState([]);

  // const getMockPhotos = () => {
  //   fetch("/api/mock-response")
  //   .then((res) => res.json())
  //   // .then((res) => {console.log(res); return res.json()})
  //   .then((data) => {
  //     setPhotoData(JSON.parse(data));
  //     setPhotos(JSON.parse(data).photos);
  //   });
  // }

  // const modelTest = async () => {
  //   const mock_urls = [
  //     'https://raisingchildren.net.au/__data/assets/image/0024/47742/baby-behaviour-and-awareness.jpg',
  //     'https://www.healthychildren.org/SiteCollectionImagesArticleImages/young-girl-in-a-hospital-bed-with-her-teddy-bear.jpg',
  //   ]
  //   console.log('modelTest start');
  //   const data = await modelTest(mock_urls)
  //   setClassified(data);
  // };

  const mock_urls = [
    'https://raisingchildren.net.au/__data/assets/image/0024/47742/baby-behaviour-and-awareness.jpg',
    'https://www.healthychildren.org/SiteCollectionImagesArticleImages/young-girl-in-a-hospital-bed-with-her-teddy-bear.jpg',
  ]

  const getPhotos = async () => {
    const data = await getPhotosFromApi(token.access_token);
    setPhotoData(data);
    setPhotos(data.mediaItems);
  };

  console.log(photoData);

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
        <Button 
            variant="contained"
            onClick={() => modelTest(mock_urls).then(data => { console.log(data)})}
          >
            Classify Mocks
          </Button>
          <Button 
            variant="contained"
            onClick={() => {console.log(photoData); return sendSampleData(photoData)}}
          >
            Send 100 (example)
          </Button>
        <PhotoDisplay photos={photos}></PhotoDisplay>
      </div>

    </div>
  );
}

export default App;
