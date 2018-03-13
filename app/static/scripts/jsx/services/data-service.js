import axios from 'axios'

const dataService = store => next => action => {
    //console.log("dataService has been activated")
    // probably the loading for async func or any sync func
    next(action)

    switch (action.type) {
        case 'GET_TODO_DATA':
            axios
                .get('todo-data.json')
                .then(function (response) {
                    console.log(response);
                    const data = response.data
                    next({
                        type: 'GET_TODO_DATA_RECEIVED',
                        data
                    })
                })
                .catch(function (error) {
                    console.log(error);
                    return next({
                        type: 'GET_TODO_DATA_ERROR',
                        error
                    })
                })
            break
        case 'LOGIN_REQUEST':
            console.log('LOGIN_REQUEST has fired')
            axios.post('/auth/login', {
                email: action.u,
                password: action.p
            })
                .then(function (response) {
                    console.log(response);
                    next({
                        type: 'SUCCESS_LOG_IN',
                        userName: action.u
                    })
                })
                .catch(function (error) {
                    console.log(error);
                    next({
                        type: 'FAILED_LOG_IN'
                    })
                });
            break
        default:
            break
    }
};


export default dataService