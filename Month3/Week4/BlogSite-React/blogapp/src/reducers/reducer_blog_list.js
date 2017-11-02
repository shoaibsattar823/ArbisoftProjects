import { FETCH_BLOGS, ADD_BLOG } from '../actions/index'
import {fetchBlogs} from '../actions/index';
import {store} from '../index';

export default function (state=[], action) {
  switch(action.type) {
    case FETCH_BLOGS:
      console.log('in reducer blogs: ', [action.payload, ...state])
      return [action.payload, ...state];
    case ADD_BLOG:
      console.log('store in reducer: ', ([store.getState().blogs[0]]));
      // current state = [store.getState().blogs[0]]
      (store.getState().blogs[0].data).concat([action.payload.data]);
      console.log('action.payload.data: ', action.payload.data);

      return [store.getState().blogs[0]];
      // return (store.getState().blogs[0].data).push(action.payload.data);
      // return fetchBlogs();

      // return [action.payload.data, ...store.getState().blogs.data];
    default:
      return state;
  }
}
