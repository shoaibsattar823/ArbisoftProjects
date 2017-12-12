import { combineReducers } from 'redux';
import BlogReducer from './reducer_blog_list';
import BlogDetailReducer from './reducer_blog_detail';
import TokenReducer from './reducer_token';

const rootReducer = combineReducers({
  blogs: BlogReducer,
  blog: BlogDetailReducer,
  token: TokenReducer,
});

export default rootReducer;
