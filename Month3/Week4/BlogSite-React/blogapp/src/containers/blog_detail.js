import React, { Component } from 'react';
import { connect } from 'react-redux';

class BlogDetail extends Component {

  constructor() {
    super();
    this.showDetails = this.showDetails.bind(this);
  }


  showDetails(title) {
    console.log('Is this the title? ', title);
  }


  render() {
    console.log(this.props);
    return (
      <div className="container-fluid">
        <h3>Blog Detail</h3>
        { this.showDetails(this.props.title) }
      </div>
    );
  }
}


function mapStateToProps({title}) {
  console.log('Title here: ', title);
  return { title };
}


export default connect(mapStateToProps)(BlogDetail);
