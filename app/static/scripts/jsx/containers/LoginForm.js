import Login from "../components/Login";
import {applyLogin} from "../actions";
import { connect } from 'react-redux'

const mapStateToProps = (state) => {
    console.log("LoginForm: state is:")
    console.log(state)
    return {
        active: true
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        applyLogin: applyLogin,
        dispatch: dispatch

    }
}

const LoginForm = connect(
    mapStateToProps,
    mapDispatchToProps
)(Login)

export default LoginForm