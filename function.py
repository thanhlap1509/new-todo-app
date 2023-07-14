FILEPATH = 'todos'
""" 
    với gui thì chuyển thành todos còn web.py thì thành experiments/todos
    không hiểu
"""
def get_todos(filepath=FILEPATH):
    """
       Read a text file and return the list of
       to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write the to-do items list in the text file
    :param todos_arg:a list of to-do items
    :param filepath: default
    :return: none
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    list = get_todos(FILEPATH)
    print(list)
