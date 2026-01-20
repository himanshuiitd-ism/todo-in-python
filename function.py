FILENAME = 'todo.txt'

def readFiles():
  with open(FILENAME,'r') as file:
    todos = file.readlines()
  return todos

def writeFiles(todos):
  with open(FILENAME,'w') as file:
    file.writelines(todos)