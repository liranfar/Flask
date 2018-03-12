import axios from 'axios'

const dataService = store => next => action => {
    console.log("dataService has been activated")
    //probably the waiting sign for asynchronous action
    next(action)


    switch ( action.type ) {
        case 'GET_TODO_DATA':
            axios
                .get('todo-data.json')
                .then(function (response) {
                    console.log(response);
                    // const data = JSON.parse(response.data)
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
        default:
            break
    }
};



export default dataService