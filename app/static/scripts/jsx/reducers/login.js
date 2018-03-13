const login = (state = false, action) => {

    switch (action.type) {
        case 'SUCCESS_LOG_IN':
            console.log("success_login action is:")
            console.log(action)
            return  true
        case 'FAILED_LOG_IN':
            return false
        //case 'IN_PROCESS':
        default:
            return false


    }

}

export default login