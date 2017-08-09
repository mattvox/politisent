import React, { Component } from 'react';
import { connect } from 'react-redux';

import { fetchTweets } from '../actions/index';

class Tweets extends Component {
  componentDidMount() {
    if (this.props.tweets.data.length === 0) {
      console.log(this.props.tweets);
      this.props.fetchTweets();
    }
  }

  renderTweets() {
    return this.props.tweets.data.map((tweet) => {
      return (
        <div key={tweet.id}>
          <p>{tweet.text}</p>
        </div>
        // <div>It works!</div>
      )
    })
  }

  render() {
    if (this.props.tweets) {
      if (this.props.tweets.data.length === 0) {
        return <div>LOADING...</div>;
      // eslint-disable-next-line
      } else {
        return <div>{this.renderTweets()}</div>;
        // return <div>this works</div>
      }
    }

  }
}

function mapStateToProps(state) {
  return {
    tweets: state.tweets.tweets,
  }
}

export default connect(mapStateToProps, { fetchTweets })(Tweets);
