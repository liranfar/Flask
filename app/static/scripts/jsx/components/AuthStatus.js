import React,{ Component } from 'react';
import {Link} from "react-router-dom";


class AuthStatus extends Component {
    constructor({ isAuthenticated }) {
        super();
        this.state = {
            isAuthenticated : isAuthenticated
        };
    }
    componentWillReceiveProps(nextProps) {
        console.log("AuthStatus will receive props!")
        if (this.state.isAuthenticated !== nextProps.isAuthenticated)
            this.setState({
                isAuthenticated: nextProps.isAuthenticated
            })
    }
    render(){
        const { isAuthenticated } = this.state
        const login_li = <Link to="/login">login</Link>
        const logout_li = <Link to="/logout">logout</Link>
        return(

            <li>
            { isAuthenticated ? logout_li : login_li }
            </li>
        )};
}


export default AuthStatus;