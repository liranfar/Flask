
import { connect } from 'react-redux'
import AuthStatus from "../components/AuthStatus";

const mapStateToProps = (state) => {
    return {
        isAuthenticated: state.login
        // TODO inject current logged user email to AuthStatus Component
        //,
        //email: state.login ? state.email : "user"
    }
}

const Auth = connect(
    mapStateToProps
)(AuthStatus)

export default Auth