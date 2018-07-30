import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Detail from './Detail';
import './rule_data';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Opaque Interaction Database</h1>
          <h2 className="App-subtitle">The University of Massachusetts, Amherst</h2>
        </header>
        <p className="App-intro">
          Brought to you by a grant study faciliated by the Linguistics Department at the University of Massachusetts, Amherst.
        </p>
        <Detail rule={window.rule_data[0]}/>
      </div>
    );
  }
}

export default App;
