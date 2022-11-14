// server/index.js
import fs from 'fs';
import express from 'express';
import passport from 'passport';
import * as dotenv from 'dotenv';

import {auth, scopes} from './auth.js';


// const express = require("express");

const PORT = process.env.PORT || 3001;

const app = express();

dotenv.config();

auth(passport);

passport.initialize();
passport.session();

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

// Star the OAuth login process for Google.
app.get('/auth/google', passport.authenticate('google', {
  scope: scopes,
  failureFlash: true,  // Display errors to the user.
  session: true,
}));


// Callback receiver for the OAuth process after log in.
app.get(
    '/auth/google/callback',
    passport.authenticate(
        'google', {failureRedirect: '/', failureFlash: true, session: true}),
    (req, res) => {
      // User has logged in.
      logger.info('User has logged in.');
      req.session.save(() => {
        res.redirect('/');
      });
    });



app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`);
});
