import {FETCH_TOKEN} from '../actions/index';

export default function(state=[], action){
  switch (action.type){
    case FETCH_TOKEN:
      return [action.payload, ...state];
    default:
      return state;
  }
}
