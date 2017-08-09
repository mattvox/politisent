
import { combineReducers } from 'redux';

import TweetsReducer from './reducer-tweets';

const rootReducer = combineReducers({
  tweets: TweetsReducer,
});

export default rootReducer;
