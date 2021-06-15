"""
Functions become ever more useful when we can pass to them some information.

Creating a function, we specify the expected information with parameters.
On a function call we pass arguments that match these parameters.
(In general words “parameters” and “arguments” can be used interchangeably.)

There are 4 ways to pass arguments to functions:
- positional arguments (mandatory, and their order matters),
- keyword arguments (named args that have default values),
- argument list/tuple (usually called *args),
- argument dictionary (**kwargs).
"""


def get_everything(*args, **kwargs):
    """Explore the way parameters look in a function.

    This function takes any number of positional and keyword arguments.
    “args” and “kwargs” variable names are conventions and can be replaced
    with other names.
    """
    assert isinstance(args, tuple)
    assert isinstance(kwargs, dict)
    print(locals())  # args and kwargs are keys in the locals() dict
    print('args:', args)
    print('kwargs:', kwargs)


def get_nothing():
    assert not locals()  # such empty


def get_args(positional, keyword=None, *args, **kwargs):
    """Function parameters must be in a specific order.

    Any other way to define and pass them will result in SyntaxError.
    """
    pass


def add_participant(first_name, last_name):
    """
    Positional arguments are used when there are few of them required.

    Their order is natural and therefore easy to remember.
    """
    return f'{first_name} {last_name} is added to a list.'


def collect_info(first_name, last_name, house=None, patronus=None):
    """
    When more information needed, order of arguments is harder to remember.

    And some pieces of information may not be mandatory. 
    In this case keyword arguments come in handy.
    They are expected (opposite to arbitrary **kwargs) but not required.
    """
    if house == 'Slytherin' and patronus:
        print('No way')


if __name__ == '__main__':
    get_everything(1979, 'otter', color='violet', occupation='dentist')
