import request from 'superagent';

const APIKey = '3f4be8e2d6926fad51510a2874891677';
const url = `http://api.openweathermap.org/data/2.5/forecast?q=London,us&appid=${APIKey}`;

const weatherData = store => next => action => {
  next(action)
  if (action.type === 'GET_WEATHER_DATA') {
    request
      .get(url)
      .then((err, res) => {
        if (err) {
          return next({
            type: 'ERROR',
            err
          })
        }

        const data = res.text
        next({
          type: 'GET_WEATHER_DATA',
          data
        })
      })
  }
}

export default weatherData



















/*const APIKey = '3f4be8e2d6926fad51510a2874891677';

export const GET_WEATHER_DATA = 'GET_WEATHER_DATA'

function getData(city, data){
  return {
    type: GET_WEATHER_DATA,
    city: city,
    payload: data
  };
}

export function get_weather_data(city) {

  return function(dispatch){
    const url = `http://api.openweathermap.org/data/2.5/forecast?q=${city},us&appid=${APIKey}`;
    let xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.send();

    xhr.onreadystatechange = () => {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        if (xhr.status === 200) {
          console.log('here?? ', xhr.responseText);
          dispatch(getData(city, xhr.responseText));
        }
        else {
          console.log('There was a problem with the request.');
        }
      }
    }
  }

}
*/
