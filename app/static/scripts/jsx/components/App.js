import React from 'react'
// import LoginForm from "../containers/LoginForm";
// import TodoSection from "../containers/TodoSection";
import Routes from "../nevigation/routes";
import {Link} from "react-router-dom";


const App = () => (
    <div>
        <div className="navigation-bar" style={{
            display: 'block',
            left: '45%',
            position: 'relative'
        }}>
            <h1> Hello React! </h1>
            <ul>
                <li><Link to="/">todo</Link></li>
                <li><Link to="/login">login</Link></li>
            </ul>
        </div>

        {/*<TodoSection />*/}
        {/*<LoginForm />*/}
        <Routes/>
    </div>
)

export default App