import { FETCH_BLOG_DETAIL } from '../actions/index';


export default function (state=[], action) {
  switch(action.type) {
    case FETCH_BLOG_DETAIL:
      return [action.payload, ...state];
    default:
      return state;
  }
}
