import streamlit as st
import function
todos = function.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    function.write_todos(todos)



st.title("App nhắc nhở việc làm cho mấy đứa đít to lười biếng")
st.subheader('Danh sách việc làm')
st.write('MEoowwwwww')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[index]
        st.experimental_rerun()

st.text_input(label=".", placeholder="Add new todo...", on_change=add_todo, key='new_todo', label_visibility='hidden')