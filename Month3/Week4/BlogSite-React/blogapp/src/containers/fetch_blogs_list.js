// import React, { Component } from 'react';
import { fetchBlogs } from '../actions/index';

import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';


function FetchBlogsList(props) {
  props.fetchBlogs();
  return null;
}


function mapDispatchToProps(dispatch){
  return bindActionCreators({fetchBlogs}, dispatch);
}

export default connect(null, mapDispatchToProps)(FetchBlogsList);
