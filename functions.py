FILENAME = 'todos.txt'

def get_todos(filename=FILENAME):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILENAME):
    """ Write a to-do items list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("hello from functions")
