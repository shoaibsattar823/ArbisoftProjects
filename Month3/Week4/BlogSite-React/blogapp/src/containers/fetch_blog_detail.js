import {fetchBlogDetail} from '../actions/index';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';

function FetchBlogDetail(props){
  console.log('here: ', props);
  return null;
}

function mapDispatchToProps(dispatch){
  return bindActionCreators({fetchBlogDetail}, dispatch);
}

export default connect(null, mapDispatchToProps)(FetchBlogDetail);
