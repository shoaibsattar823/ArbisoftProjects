import { combineReducers } from 'redux';
import BlogReducer from './reducer_blog_list';
import BlogDetailReducer from './reducer_blog_detail';

const rootReducer = combineReducers({
  blogs: BlogReducer,
  blog: BlogDetailReducer
});

export default rootReducer;
