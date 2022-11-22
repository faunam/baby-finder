import axios from 'axios';

const token_header_config = (token) => {
    return (
      {
        headers: {
          Authorization: "Bearer " + token,
          "Content-type": "application/json",
        }
      }
    )
  }
  
  
export const getPhotosFromApi = async (token, pageToken = undefined) => {
    const config = {
        ...token_header_config(token), 
        params: {
            "pageSize": "100", // apparently cant exceed 100
            ...(!!pageToken && {pageToken}),
    }};

    const res = await axios.get("https://photoslibrary.googleapis.com/v1/mediaItems", config)
    return res.data;
};
