import streamlit as stream
from functions import *



todos = get_todos()

def add_todo():
    todo = stream.session_state['addtask'] + '\n'
    todos.append(todo)
    write_todos(todos)





stream.title("Todo App")
stream.subheader("This is a subheader")
stream.write("random text")

for index,todo in enumerate(todos) :
    checkbox = stream.checkbox(todo, key=todo)
    if checkbox :
        todos.pop(index)
        write_todos(todos)
        del stream.session_state[todo]
        stream.rerun()




stream.text_input(label="" ,placeholder="Enter in tasks you need to do", on_change=add_todo, key='addtask')