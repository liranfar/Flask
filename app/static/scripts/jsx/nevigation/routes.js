import {Route, Switch} from "react-router-dom";
import LoginForm from "../containers/LoginForm";
import TodoSection from "../containers/TodoSection";
import React from 'react'
const Routes = () => (

            <Switch>
                <Route exact path='/' component={TodoSection}/>
                <Route path='/login' component={LoginForm}/>
                {/*<Route path='/about' component={About}/>*/}
                {/*<Route path='/signup' component={Signup}/>*/}
                {/*from server side point of view we want to make sure that requests is coming from authenticated users*/}
                {/*<Route path='/new-event' component={requireAuth(NewEventPage)}/>*/}
            </Switch>

    )
export default Routes;