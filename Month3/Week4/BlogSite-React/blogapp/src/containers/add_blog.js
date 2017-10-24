import React, {Component} from 'react';
// import {Router, Route, IndexRoute, hashHistory} from 'react-router';
// import {Link} from 'react-router-dom';

class ShowForm extends Component{
  constructor(){
    super();
    this.state = {
      title: '',
      post: ''
    }
  }

  onFormSubmit(event){
    event.preventDefault();
    console.log("Form submitted: ", event.target);
    console.log("Title: ", event.target.title.value);
    console.log("Post: ", event.target.post.value);
  }

  onInputChange(event){
    this.setState({title: event.target.value});
  }
  onTextChange(event){
    this.setState({post: event.target.value});
  }

  render(){
    const fstyle = {"fontWeight": 'normal'};
    if (this.props.click === true){
      return (
        <form onSubmit={this.onFormSubmit.bind(this)} type="POST">
          <dd>Title:</dd>
          <dt>
            <input
              id="title"
              value={this.state.value}
              onChange={this.onInputChange.bind(this)}
            />
          </dt>

          <dd>Post:</dd>
          <dt>
          <textarea id="post" rows="5" cols="50" style={fstyle}
            value={this.state.value} onChange={this.onTextChange.bind(this)}>
          </textarea>
          </dt>
          <button type="sumbit">Save</button>
        </form>
      );
    }
    else{
      return null;
    }
  }
}

class AddBlog extends Component {
  constructor(){
    super();
    this.state = {
      click: false
    }
  }

  onclick(evt){
    evt.preventDefault();
    this.setState({click:!this.state.click});
  }

  render(){
    return (
      <div className="col-md-4 list-group">
        <a onClick={this.onclick.bind(this)} href="#/add-blog">Add Blog</a>
        <ShowForm click={this.state.click} />
      </div>
    );
  }
}

export default AddBlog;
