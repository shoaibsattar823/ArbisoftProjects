import React, { Component } from 'react';
import { connect } from 'react-redux';

import FetchBlogDetail from './fetch_blog_detail';
import BlogDetail from './blog_detail';
import AddBlog from './add_blog';


class BlogsList extends Component {
  constructor() {
    super();
    this.state = {
      title: '',
    }
    this.showDetails = this.showDetails.bind(this);
  }

  showDetails(event) {
    event.preventDefault();
    const title = event.target.innerText;
    this.setState({title: title});
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
    return (
      <div>
        <div className="container-fluid">
          <h3>Blogs List</h3>
          { this.renderBlogs(this.props.blogs) }
          <FetchBlogDetail title={this.state.title}/>
          <BlogDetail />
        </div>
        <AddBlog />
      </div>
    );
  }
}

function mapStateToProps({blogs}) {
  return { blogs};
}

export default connect(mapStateToProps)(BlogsList);
