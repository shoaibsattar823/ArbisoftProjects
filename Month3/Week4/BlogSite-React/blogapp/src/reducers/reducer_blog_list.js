import { FETCH_BLOGS } from '../actions/index'


export default function (state=[], action) {
  switch(action.type) {
    case FETCH_BLOGS:
      return [action.payload, ...state];
    default:
      return state;
  }
}
