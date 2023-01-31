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
  
const default_header_config = {
    headers: {
      "Content-type": "application/json",
    }
};
  
  
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

export const sendSampleData = async (data) => {
  const res = await axios.post("http://127.0.0.1:5000/sample", data);

  console.log(res);
  return res.data;
}

export const modelTest = async (urls) => {
  const body = {
    'urls': urls
  }
  const res = await axios.post("http://127.0.0.1:5000/model", body)
  console.log(res)
  return res.data;
};

export const helloWorld = async () => {
  console.log(default_header_config);
  return await axios.get("http://127.0.0.1:5000/hello", default_header_config);
}
