import React, { Component } from 'react';
import { connect } from 'react-redux';
// import  BlogDetail  from './blog_detail'
// import FetchBlogDetail from './fetch_blog_detail';


class BlogsList extends Component {
  constructor() {
    super();
    this.showDetails = this.showDetails.bind(this);
  }


  showDetails(event) {
    event.preventDefault();
    const title = event.target.innerText;
    console.log('Title: ', title);
    // return (
    //   <div>
    //     <FetchBlogDetail />
    //     <BlogDetail title={title}/>
    //   </div>
    // );
  }


  renderBlogs(data) {
    let titles;
    if (data[0]){
      titles = data[0].data.map(blog => blog.title);
      return titles.map(title =>
        <a key={title} href="" onClick={this.showDetails}><div>{title}</div></a>
      );
    }
  }


  render() {
    console.log('log3: ', this.props.blogs);
    return (
      <div className="container-fluid">
        <h3>Blogs List</h3>
        { this.renderBlogs(this.props.blogs) }
      </div>
    );
  }
}


function mapStateToProps({blogs}) {
  return { blogs };
}


export default connect(mapStateToProps)(BlogsList);
