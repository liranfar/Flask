import React from 'react'
import {Link} from "react-router-dom";
import Routes from "../nevigation/routes";
import Auth from "../containers/Auth";


const App = () => {
    return(
    <div>
        <div className="navigation-bar" style={{
            display: 'block',
            left: '45%',
            position: 'relative'
        }}>
            <h1> Hello React! </h1>

            <ul>
                <li><Link to="/">index</Link></li>
                <li><Link to="/todo">todo</Link></li>
                <Auth />
            </ul>
        </div>

        <Routes/>
    </div>
)}


export default App