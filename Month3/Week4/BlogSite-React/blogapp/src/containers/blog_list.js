import React, { Component } from 'react';
import { connect } from 'react-redux';

import {fetchBlogDetail} from '../actions/index';
// import {bindActionCreators} from 'redux';
import BlogDetail from './blog_detail';
// import BlogDetail from '../components/blog_detail';

class BlogsList extends Component {
  constructor() {
    super();
    this.state = {
      title: '',
      click: false,
    }

    this.showDetails = this.showDetails.bind(this);
  }


  showDetails(event) {
    event.preventDefault();
    const title = event.target.innerText;
    console.log('Title: ', title);
    console.log('Props.BLOGS: ', this.props.blogs);
    console.log('Props.Title: ', this.props.title);
    this.setState({title: title});
    const detail = fetchBlogDetail(title);
    console.log('Detail: ', detail.payload);
  }


  renderBlogs(data) {
    let titles;
    if (data[0]){
      titles = data[0].data.map(blog => blog.title);
      return titles.map(title =>
        <a key={title} href="" onClick={this.showDetails}>
          <div>{title}</div>
        </a>
      );
    }
  }

  renderDetail() {
    return <div>{this.state.title}</div>
  }

  render() {
    console.log('reached inside blog_list container');
    return (
      <div>
        <div className="container-fluid">
          <h3>Blogs List</h3>
          { this.renderBlogs(this.props.blogs) }
          <BlogDetail  />
        </div>
      </div>
    );
  }
}

// function mapDispatchToProps(dispatch) {
//   return bindActionCreators({fetchBlogDetail}, dispatch);
// }
//
// connect(mapDispatchToProps)(BlogsList);

function mapStateToProps({blogs}) {
  return { blogs};
}

export default connect(mapStateToProps)(BlogsList);
