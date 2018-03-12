import { combineReducers } from 'redux'
import todos from './todos'
import visibilityFilter from './visibilityFilter'
import loading from './loading'

const todoApp = combineReducers({
    loading,
    todos,
    visibilityFilter
})
 
export default todoApp