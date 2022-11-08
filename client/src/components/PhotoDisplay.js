
import React, {useEffect, useState} from 'react';
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';

function PhotoDisplay({photos}) {

    console.log(photos)

return (
    <ImageList sx={{ width: 500, height: 450 }} cols={3} rowHeight={164}>
    {photos.map((item) => (
        <ImageListItem key={item.baseUrl}>
        <img
            src={`${item.baseUrl}?w=164&h=164&fit=crop&auto=format`}
            srcSet={`${item.baseUrl}?w=164&h=164&fit=crop&auto=format&dpr=2 2x`}
            alt={item.filename}
            loading="lazy"
        />
        </ImageListItem>
    ))}
    </ImageList>

)

}


export default PhotoDisplay;

