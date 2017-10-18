import React, { Component } from 'react';

import FetchBlogs from '../containers/fetch_blogs_list';
import BlogsList from '../containers/blog_list';


class App extends Component {
  render() {
    return (
      <div>
        <FetchBlogs />
        <BlogsList />
      </div>
    );
  }
}

export default App;
