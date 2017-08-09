import { FETCH_TWEETS } from '../actions/index';

const INITIAL_STATE = { tweets: { data: [] } };

export default function (state = INITIAL_STATE, action) {
  switch (action.type) {
    case FETCH_TWEETS:
      return { ...state, tweets: action.payload.data };

    default:
      return state;
  }
}
