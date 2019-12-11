import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

const port = '8934'
//const apiServer = 'http://home.therealbenforce.com'
const apiServer = 'http://192.168.0.105'

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      status: 'offline',
      serial: null,
    };
  }

  componentDidMount() {
    const blinkIdUrl = apiServer + ':' + port + '/blink1/id'
    const blinkId = fetch(blinkIdUrl)
      .then(res => res.json())
      .then(data => (
        this.setState({status: 'online' }),
        this.setState({serial : data.blink1_serialnums[0]})
        )
      )
      .catch(console.log)
  }

  render() {
    const { status } = this.state;
    const { serial } = this.state;
    return (
      <div> 
        { status }
        <br></br>
        { serial }
      </div>
    )
  }
}

export default App;