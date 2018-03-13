import React from 'react'
import {render} from 'react-dom'
import {Provider} from 'react-redux'
import {createStore, applyMiddleware, compose} from 'redux'
import todoApp from './reducers/root'
import App from './components/App'
import dataService from "./services/data-service";
import {BrowserRouter as Router} from 'react-router-dom';

let store = createStore(todoApp, {}, compose(applyMiddleware(dataService), window.devToolsExtension ? window.devToolsExtension() : f => f));

render(
    <Provider store={store}>
        <Router>
            <App/>
        </Router>
    </Provider>,
    document.getElementById('root')
)

store.dispatch({type: 'GET_TODO_DATA'})
