import axios from 'axios';

const token_header_config = (token) => {
    return (
      {
        headers: {
          Authorization: "Bearer " + token
        }
      }
    )
  }
  
  
export const getPhotosFromApi = (token) => {
    const config = token_header_config(token) // add token to request body

    axios.get("https://photoslibrary.googleapis.com/v1/albums", config)
    // .then(res => res.json())
    .then(res => {
        console.log(res);
        return res.data;
    })
    .catch(err => {
        console.log(err);
        return {};
    });
};
