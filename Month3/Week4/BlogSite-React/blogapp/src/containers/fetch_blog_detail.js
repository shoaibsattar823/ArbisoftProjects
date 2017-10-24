import {fetchBlogDetail} from '../actions/index';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';


function FetchBlogDetail(props){
  console.log('Inside FetchBlogDetail: ', props);
  const title = props.title;
  if (title){
    props.fetchBlogDetail(title);
  }
  return null;
}

function mapDispatchToProps(dispatch){
  return bindActionCreators({fetchBlogDetail}, dispatch);
}

export default connect(null, mapDispatchToProps)(FetchBlogDetail)
