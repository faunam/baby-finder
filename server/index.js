// server/index.js
import fs from 'fs';
import express from 'express';
import axios from 'axios';


// const express = require("express");

const PORT = process.env.PORT || 3001;

const app = express();

app.get("/api/mock-response", (req, res) => {
  fs.readFile('mockApiResponse.json', 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    res.json(data);
  })
});

app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`);
});