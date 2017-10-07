import axios from 'axios';

const APIKey = '3f4be8e2d6926fad51510a2874891677';
const ROOT_URL = 'http://api.openweathermap.org/data/2.5/forecast?q=';
export const FETCH_WEATHER = 'FETCH_WEATHER';

export function fetchWeather(city) {
  const url = `${ROOT_URL}${city},us&appid=${APIKey}`;
  const request = axios.get(url);

  return {
    type: FETCH_WEATHER,
    payload: request
  };
}
