import React, { Component } from 'react';
import ReactDOM  from 'react-dom';

class App extends Component {
  constructor() {
    super();
    this.state = {
      articles: [
        { title: "React-Redux", id: 1 },
        { title: "Hello From React!", id: 2 }
      ]
    };
  }
  render() {
    const { articles } = this.state;
    return <ul>{articles.map(el => <li key={el.id}>{el.title}</li>)}</ul>;
  }
}

ReactDOM.render(
    React.createElement(App, null),
    document.getElementById('root')
);

