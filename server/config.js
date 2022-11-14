import * as dotenv from 'dotenv';

// The OAuth client ID from the Google Developers console.
export const oAuthClientID = process.env.REACT_APP_GOOGLE_CLIENT_ID;

// The OAuth client secret from the Google Developers console.
export const oAuthclientSecret = process.env.REACT_APP_GOOGLE_CLIENT_SECRET;

export const oAuthCallbackUrl = 'http://127.0.0.1:8080/auth/google/callback';