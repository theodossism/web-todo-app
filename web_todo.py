import streamlit as ST
import functions


todolist = functions.get_todos()


def add_todo():
    new_todo = ST.session_state["new_todo"] + "\n"
    todolist.append(new_todo)
    functions.write_todos(todolist)


ST.title("My Todo WebApp")
ST.subheader("This is my custom Todo App")
for index, todo in enumerate(todolist):
    checkbox = ST.checkbox(todo, key=todo)
    if checkbox:
        todolist.pop(index)
        functions.write_todos(todolist)
        del ST.session_state[todo]
        ST.rerun()

ST.text("")
ST.text_input(label="New Todo Here", placeholder="Add a new todo...", key="new_todo", on_change=add_todo)
