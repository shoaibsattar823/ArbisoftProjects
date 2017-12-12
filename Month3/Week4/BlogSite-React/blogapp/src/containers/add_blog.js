import React, {Component} from 'react';
import {addBlog} from '../actions/index';
// import Login from './login';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';


class ShowForm extends Component{
  constructor(){
    super();
    this.state = {
      title: '',
      post: '',
      blogger: '',
      date: '',
      token: '',
      options: ["shoaib", "muhammad", "hammad"]
    }
  }

  onFormSubmit(event){
    event.preventDefault();
    console.log("Form submitted: ", event.target);
    const title = event.target.title.value;
    const post = event.target.post.value;
    const published_date = event.target.pub_date.value;
    const blogger = event.target.blogger.value;
    const data = {
      title: title, post: post, published_date: published_date, blogger: blogger
    };
    console.log('addBlog in ShowForm onFormSubmit: ', this.props.token);
    this.props.addBlog({data:data, token: this.props.token});
  }

  onInputChange(event){
    this.setState({title: event.target.value});
  }
  onTextChange(event){
    this.setState({post: event.target.value});
  }

  render(){
    const fstyle = {"fontWeight": 'normal'};
    console.log('addBlog in ShowForm: ', this.props.addBlog);
    // if (this.state.token === ''){
    //   this.setState({token: this.props.token});
    // }
    if (this.props.click === true){
      return (
        <form onSubmit={this.onFormSubmit.bind(this)} type="POST">
          <dd>Title:</dd>
          <dt>
            <input
              id="title"
              value={this.state.title}
              onChange={this.onInputChange.bind(this)}
            />
          </dt>

          <dd>Post:</dd>
          <dt>
            <textarea
              id="post" rows="5" cols="50" style={fstyle}
              value={this.state.post} onChange={this.onTextChange.bind(this)}>
            </textarea>
          </dt>
          <dd>Published Date: </dd>
          <dt>
            <input
              id="pub_date"
              onChange={(e)=>this.setState({date: e.target.value})}
              type="date" value={this.state.date}/>
          </dt>
          <dd>Blogger:</dd>
          <dt>
            <select id="blogger" value={this.state.blogger}
              onChange={e=>this.setState({blogger:e.target.value})}>
              {this.state.options.map(opt => <option key={opt}>{opt}</option>)}
            </select>
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
    console.log('dispatch addBlog: ', this.props.addBlog);
    if (this.props.token[0] === undefined){
      return null;
    }
    console.log("Token in AddBlog: ", this.props.token[0].data.token);
    const token = this.props.token[0].data.token;
    return (
      <div className="container-fluid">
        <h3>Add a New Blog</h3>
        <a onClick={this.onclick.bind(this)} href="">Add Blog</a>
        <ShowForm click={this.state.click} token={token} addBlog={this.props.addBlog}/>
      </div>
    );
  }
}

function mapStateToProps({token}){
  return {token};
}
function mapDispatchToProps(dispatch){
  return bindActionCreators({addBlog}, dispatch);
}
export default connect(mapStateToProps, mapDispatchToProps)(AddBlog);
