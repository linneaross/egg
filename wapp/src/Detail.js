import React, { Component } from 'react';
import './Detail.css';

class Detail extends Component {
  constructor(props) {
    super(props);
    this.state = {
      rule: props.rule
    };
  }
  render() {
    return (
      <div className="Detail">
      {this.state.rule.language}
      </div>
    );
  }
}

export default Detail;
