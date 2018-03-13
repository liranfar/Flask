import { combineReducers } from 'redux'
import todos from './todos'
import visibilityFilter from './visibilityFilter'
import loading from './loading'
import login from "./login";

const todoApp = combineReducers({
    loading,
    todos,
    visibilityFilter,
    login
})
 
export default todoApp