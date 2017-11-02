import React, { Component } from 'react';

import Login from '../containers/login'

import FetchBlogs from '../containers/fetch_blogs_list';
import BlogsList from '../containers/blog_list';

class App extends Component {
  render() {
    return (
      <div>
        <Login />
        <FetchBlogs />
        <BlogsList />
      </div>
    );
  }
}

export default App;
