import React from 'react'
import PropTypes from 'prop-types'
import {Redirect} from "react-router-dom";

class Login extends React.Component {

    constructor({isAuthenticated, applyLogin, dispatch}) {
        super();
        this.state = {
            isAuthenticated: isAuthenticated,
            fireRedirect: false
        }
    }

    componentWillReceiveProps(nextProps) {
        console.log("will receive props!! nextProps are:")
        console.log(nextProps)
        if ( true === nextProps.isAuthenticated) {
            this.setState({isAuthenticated: nextProps.isAuthenticated,
                            fireRedirect: true
                })

        }
    }

    render() {

        console.log('isAuthenticated:')
        console.log(this.state.isAuthenticated)

        const { from } = this.props.location || '/';

        let user_name, pass

        return (

            <div style={{
                display: 'block',
                left: '45%',
                position: 'relative'
            }}>
                <h1>
                    Login
                </h1>

                <form
                    onSubmit={e => {
                        e.preventDefault()
                        // if (!input.value.trim()) {
                        //     return
                        // }
                        this.props.dispatch(this.props.applyLogin(user_name.value, pass.value))
                        user_name.value = ''
                        pass.value = ''
                    }}
                >
                    <input style={{
                        display: 'block',
                        margin: '20px 0px'
                    }}
                           type="email"
                           placeholder="Email"
                           ref={node => {
                               user_name = node
                           }}
                    />
                    <input style={{
                        display: 'block',
                        margin: '20px 0px'
                    }}
                           type="password"
                           placeholder="Password"
                           ref={node => {
                               pass = node
                           }}
                    />
                    <button style={{
                        display: 'block',
                        margin: '20px 0px'
                    }} type="submit">
                        Sign in
                    </button>
                </form>
                {this.state.fireRedirect && (<Redirect to={from || '/'}/>)}
            </div>


        )
    }
}

Login.propTypes = {
    isAuthenticated: PropTypes.bool.isRequired,
    applyLogin: PropTypes.func.isRequired,
    dispatch: PropTypes.func.isRequired
}


export default Login

