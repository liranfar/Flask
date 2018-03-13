const login = (state = 'UN_LOGGED', action) => {

    switch (action.type) {
        case 'SUCCESS_LOG_IN':
            console.log("success_login action is:")
            console.log(action)
            return  action
        case 'FAILED_LOG_IN':
            return state
        //case 'IN_PROCESS':
        default:
            return state


    }

}

export default login