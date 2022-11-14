// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

import {Strategy as GoogleOAuthStrategy} from 'passport-google-oauth20';

export const auth = (passport) => {

  passport.serializeUser((user, done) => done(null, user));
  passport.deserializeUser((user, done) => done(null, user));
  passport.use(new GoogleOAuthStrategy(
      {
        clientID: process.env.REACT_APP_GOOGLE_CLIENT_ID,
        clientSecret: process.env.REACT_APP_GOOGLE_CLIENT_SECRET,
        callbackURL: 'http://localhost:3000/auth/google/callback'
      },
      (token, refreshToken, profile, done) => done(null, {profile, token})));
};

export const scopes = [
  'https://www.googleapis.com/auth/photoslibrary.readonly',
  'profile',
];