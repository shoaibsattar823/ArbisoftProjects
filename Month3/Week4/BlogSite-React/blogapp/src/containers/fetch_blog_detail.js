import { fetchBlogDetail } from '../actions/index';

import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';


function FetchBlogDetail(props) {
  console.log(props.title);
  const data = props.fetchBlogDetail(props.title);
  return null;
}

function mapDispatchToProps(dispatch){
  console.log('here???');
  return bindActionCreators({fetchBlogDetail}, dispatch);
}

export default connect(null, mapDispatchToProps)(FetchBlogDetail);
