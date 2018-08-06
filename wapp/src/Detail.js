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
      <p>Language: {this.state.rule.language}</p>
      <p>Interaction Name: {this.state.rule.name}</p>
      <p>Interaction Type: {this.state.rule.opacityType}</p>
      <p>Process 1:</p>
      <p>Rule Type: {this.state.rule.processes[0].ruleType}</p>
      <p>Description: {this.state.rule.processes[0].description}</p>
      <p>Productivity: {this.state.rule.processes[0].productivity}</p>
      <p>Limitations: {this.state.rule.processes[0].limitations}</p>
      <p>Additional Infterpretations: {this.state.rule.processes[0].additionalInt}</p>
      <p>Process 2:</p>
      <p>Rule Type: {this.state.rule.processes[1].ruleType}</p>
      <p>Description: {this.state.rule.processes[1].description}</p>
      <p>Productivity: {this.state.rule.processes[1].productivity}</p>
      <p>Limitations: {this.state.rule.processes[1].limitations}</p>
      <p>Additional Infterpretations: {this.state.rule.processes[0].additionalInt}</p>
      <p>References: {this.state.rule.references}</p>
      <p>Free Variation: {this.state.rule.freeVariation}</p>
      <p>Alternate Analyses: {this.state.rule.altAnalyses}</p>
      <p>Comments: {this.state.rule.comments}</p>
      </div>
    );
  }
}

export default Detail;
