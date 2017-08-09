import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware, compose } from 'redux';

import promise from 'redux-promise';
import reducers from './reducers';

// import './index.css';

import App from './App';
import registerServiceWorker from './registerServiceWorker';

/* eslint-disable no-underscore-dangle */
const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const reduxStore = createStore(reducers, /* preloadedState, */ composeEnhancers(
  applyMiddleware(promise),
));
/* eslint-enable */

ReactDOM.render(
  <Provider store={reduxStore}>
    <App />
  </Provider>
  , document.getElementById('root'));
registerServiceWorker();
