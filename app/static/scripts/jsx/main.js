/*** @jsx React.DOM */
class App extends React.Component {
    render() {
        return (
            <div>
                <h1> Hello - World !</h1>
            </div>
        )
    }
}

ReactDOM.render(
    React.createElement(App, null),
    document.getElementById('root')
);

