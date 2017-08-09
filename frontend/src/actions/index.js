import axios from 'axios';

const ROOT_URL = 'http://localhost:8000';
const API_ENTRY_POINT = 'api';

export const FETCH_TWEETS = 'FETCH_TWEETS';

export function fetchTweets() {
  const request = axios.get('http://localhost:8000/api/');
  // const request = axios.get(`${ROOT_URL}/${API_ENTRY_POINT}`);

  return {
    type: FETCH_TWEETS,
    payload: request,
  }
}
