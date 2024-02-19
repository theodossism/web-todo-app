FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read the current todos.txt file and create a list """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ This function behaves as a procedure that is why it doesn't need to 'return' any result
    Write todos list contents to the file """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


# This block is to distinguish what is run when this script is called directly
# When the script is called directly then its name is "__main__"
# when this script is called by another script then its name is "functions"
if __name__ == "__main__":
    print('Hello')
    print(get_todos())
