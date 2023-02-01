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
  
  
export const getPhotosFromApi = async (token, pageToken = false) => {
    const config = {
        ...token_header_config(token), 
        params: {
            "pageSize": "100", // apparently cant exceed 100
            ...(!!pageToken && {pageToken}),
    }};

    const res = await axios.get("https://photoslibrary.googleapis.com/v1/mediaItems", config)
    return res.data;
};

export const classify = async (photoData) => {
  const res = await axios.post("http://127.0.0.1:5000/model", photoData)
  console.log(res);
  return res.data;
};
