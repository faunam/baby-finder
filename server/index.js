// server/index.js
import fs from 'fs';
import express from 'express';


// const express = require("express");

const PORT = process.env.PORT || 3001;

const app = express();

app.get("/api/example", (req, res) => {
  res.json({ message: "Hello from server!" });
});

app.get("/api/example/calculate", (req, res) => {
  res.json({ message: String(203948209348 * 2084208340) });
});

app.get("/api/mock-response", (req, res) => {
  fs.readFile('mockApiResponse.json', 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log('server side!')
    console.log(data);
    res.json(data);
  })
});


app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`);
});