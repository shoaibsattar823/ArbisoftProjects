import React, {Component} from 'react';
import SearchBar from '../containers/search_bar';
import WeatherList from '../containers/weather_list';
class App extends Component {
  render() {

    return (
      <div>
        <h3 className="text-center">Weather Forecast for next Five Days</h3>
        <SearchBar />
        <WeatherList />
      </div>
    );
  }
}

export default App;
