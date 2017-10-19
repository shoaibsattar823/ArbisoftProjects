import {connect} from 'react-redux';

function BlogDetail(props){
  console.log('reacheddddd', props.data);
  return null;
}

function mapStateToProps({title}){
  return {title};
}

export default connect(mapStateToProps)(BlogDetail);
