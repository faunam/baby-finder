// server/index.js
import fs from 'fs';
import express from 'express';
import { nextTick } from 'process';


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
    res.json(data);
  })
});

// we dont want a callback because i dont want to receive the token on the back end, want to keep it in the front
// plus i dont know how to send data to frontend from back without frontend 'getting' it, and in that case
// i would have to store it somewhere. and again, i dont want to do that
// app.post( "/auth/google/callback", 
// // (req, res) => {
// //   console.log(res.json());
// // },
// (req, res) => {
//   console.log(res.json());
//   res.redirect("/");
//   return;
// }
// );

app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`);
});