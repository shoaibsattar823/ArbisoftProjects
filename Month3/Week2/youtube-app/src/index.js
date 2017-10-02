import _ from 'lodash';
import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import SearchBar from './search_bar';
import VideoList from './video_list';
import VideoDetail from './video_detail';
import YTSearch from 'youtube-api-search';

const API_KEY = 'AIzaSyB6rbxMZVP8v3VosV4KdP6_fVdphtWqQP0';

class App extends Component {
  constructor() {
    super();
    this.state = {
      videos: [],
      selectedVideo: null
    }

    this.videoSearch('junaid jamshaid');
  }

  videoSearch(term) {
    YTSearch({key: API_KEY, term: term}, (data) => {
      this.setState({videos: data, selectedVideo: data[0]});
    })
  }

  render() {
    const videoSearch = _.debounce((term) => {this.videoSearch(term)}, 500)

    return (
      <div>
        <SearchBar onSearchTermChange={videoSearch}/>
        <VideoDetail video={this.state.selectedVideo}/>
        <VideoList
          onVideoSelect = {videoSelected => this.setState({selectedVideo: videoSelected})}
          videos={this.state.videos}
        />
      </div>
    );
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
