import streamlit as st
import function
import time

todos = function.readFiles()

def add_todo():
  todo = st.session_state["new_todo"]+ f"( {time.strftime("%b %d, %Y %H:%M:%S")})" +"\n"
  todos.insert(0,todo)
  function.writeFiles(todos)
st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This is to inc your productivity")

for index,t in enumerate(todos):
  checkbox = st.checkbox(t,key=t)
  if checkbox:
    todos.pop(index)
    function.writeFiles(todos)
    del st.session_state[t]  #(no need of this bcoz anyway st.rerun() refreshes the page on clicks)
    st.rerun()

st.text_input(label="",placeholder="Add new Todo...",
              on_change=add_todo,key="new_todo") #mtlb jbbhi enter click hoga to add_todo call ho jaaega

st.session_state