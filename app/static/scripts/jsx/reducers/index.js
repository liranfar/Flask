import { combineReducers } from 'redux'
import todos from './todos'
import visibilityFilter from './visibilityFilter'
import loading from './loading'

const todoApp = combineReducers({
    // all these reducers are attached to store's state e.g state.loading state.todos ...
    loading,
    todos,
    visibilityFilter
})
 
export default todoApp