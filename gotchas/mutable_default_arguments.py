# the most famous Python gotcha
# default arguments in Python functions are evaluated on function definition.
# solution: create a new object on each function call if nothing is passed.


def do_this(task, todo_list=[]):
    """Something goes wrong here."""
    todo_list.append(task)
    return todo_list


def do_that(task, todo_list=None):
    """Phew, that's going to be fine."""
    if not todo_list:
        todo_list = []
    todo_list.append(task)
    return todo_list


if __name__ == '__main__':
    my_list = do_this('make a todo list')
    my_list.append('check off the first item')
    other_list = do_this('do this important thing')

    for task in my_list:
        print('->', task)
    print('oh no\n')

    my_new_list = do_that('make a todo list')
    my_new_list.append('check off the first item')
    other_new_list = do_that('do that important thing')

    for task in my_new_list:
        print('->', task)
    print('nice!')
