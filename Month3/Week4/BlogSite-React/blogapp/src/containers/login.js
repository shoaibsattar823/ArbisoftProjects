import React, {Component} from 'react';
import {fetchToken, addBlog} from '../actions/index';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';
import AddBlog from './add_blog';


class Login extends Component{
  constructor(){
    super();
    this.state = {
      username: '',
      password: '',
      token: ''
    }
    this.handleClick = this.handleClick.bind(this);
  }

  // handleResponse(response){
  //   this.setState({token: response.data.token});
  //   console.log('here is response: ', this.state.token);
  //   this.props.addBlog({token: this.state.token})
  // }

  handleClick(event){
    const payload = {
      'username': this.state.username,
      'password': this.state.password
    }
    this.props.fetchToken(payload);
  }

  onUsernameChange(event){
    this.setState({username: event.target.value});
    console.log(event.target.value)
  }

  onPassChange(event){
    this.setState({password:event.target.value});
  }

  render(){
    console.log("here in login: data: ", this.props.data);
    return (
      <div>
        <input
          placeholder="Enter your username"
          value={this.state.username}
          onChange={this.onUsernameChange.bind(this)}
        />
        <input
          type="password" placeholder="Enter your password"
          value={this.state.password}
          onChange={this.onPassChange.bind(this)}
        />
        <button type="submit" onClick={this.handleClick}>Login</button>
      </div>
    );
  }
}

function mapDispatchToProps(dispatch){
  return bindActionCreators({fetchToken}, dispatch);
}

export default connect(null, mapDispatchToProps)(Login);
