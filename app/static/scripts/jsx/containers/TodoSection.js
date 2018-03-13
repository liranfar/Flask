import AddTodo from "./AddTodo";
import VisibleTodoList from "./VisibleTodoList";
import Footer from "../components/Footer";
import React from 'react'

const TodoSection = () => {
    return (
        <div style={{
            display: 'block',
            left: '45%',
            position: 'relative'
        }}>
            <AddTodo/>
            <VisibleTodoList/>
            <Footer/>
        </div>
    )
}

export default TodoSection
