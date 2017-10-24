import React from 'react';
import {connect} from 'react-redux';


function BlogDetail(props){
  if (props.blog[0] === undefined){
    return null;
  }
  const data = props.blog[0].data;
  const title = data.title;
  const post = data.post;
  const pub_date = data.published_date;
  const blogger = data.blogger;
  return (
    <div className='container-fluid'>
      <h2>Details</h2>
      <dl className="row">
        <dt className="col-sm-2">Title: </dt>
        <dd className="col-sm-9">{title}</dd>

        <dt className="col-sm-2">Post: </dt>
        <dd className="col-sm-9">{post}</dd>

        <dt className="col-md-2">Publised Date: </dt>
        <dd className="col-md-9">{pub_date}</dd>

        <dt className="col-sm-2">Blogger: </dt>
        <dd className="col-sm-9">{blogger}</dd>
      </dl>
    </div>
  );
}

function mapStateToProps({blog}){
  return {blog};
}

export default connect(mapStateToProps)(BlogDetail);
