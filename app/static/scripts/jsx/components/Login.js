import React from 'react'
import PropTypes from 'prop-types'
import {applyLogin} from "../actions/index";

const Login = ({active, applyLogin, dispatch}) => {

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
                    dispatch(applyLogin(user_name.value, pass.value))
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
        </div>
    )
}
Login.propTypes = {
    active: PropTypes.bool.isRequired,
    applyLogin: PropTypes.func.isRequired,
    dispatch: PropTypes.func.isRequired
}


export default Login