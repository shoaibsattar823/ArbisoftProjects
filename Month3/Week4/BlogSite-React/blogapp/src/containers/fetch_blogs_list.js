// import React, { Component } from 'react';
import { fetchBlogs } from '../actions/index';

import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';


function FetchBlogsList(props) {
  console.log('reached inside fetch_blogs_list container');
  props.fetchBlogs();
  return null;
}
// class FetchBlogsList extends Component {
//   data = this.props.fetchBlogs();
//
//   render() {
//     // console.log('log2: ', this.data)
//     // return (
//     //   <div>
//     //     {this.renderBlogsList(this.data)}
//     //   </div>
//     // );
//     return null;
//   }
// }


function mapDispatchToProps(dispatch){
  return bindActionCreators({fetchBlogs}, dispatch);
}

export default connect(null, mapDispatchToProps)(FetchBlogsList);
