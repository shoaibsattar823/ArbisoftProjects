import { FETCH_BLOG_DETAIL } from '../actions/index';


export default function (state=[], action) {
  console.log('Action Type: ', action.type);
  switch(action.type) {
    case FETCH_BLOG_DETAIL:
      console.log('state here: ',action.payload);
      return [action.payload, ...state];
    default:
      return state;
  }
}
