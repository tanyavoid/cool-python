"""
Function becomes ever more useful when we can pass to it some pieces of
information which can influence its result or change the information.

This information is called function parameters (or arguments).
Parameters are what's specified on a function definition,
arguments — what is passed on a function call.
But in general the two words are used interchangeably.

Positional arguments and mandatory, keyword arguments are not.
Positional arguments always go before keyword arguments.
Keyword arguments have default values.

“args” and “kwargs” names are conventions.
Asterisk (*) in Python performs unpacking:
single * — list (or tuple) unpacking,
double ** — dict unpacking.

"""


def get_everything(*args, **kwargs):
    """Explore the way parameters look in a function.

    This function takes any number of positional and keyword arguments.
    """
    assert isinstance(args, tuple)
    assert isinstance(kwargs, dict)
    print(locals())  # all the args and kwargs
    print(args)
    print(kwargs)


def get_nothing():
    print(locals())  # such empty


# Function parameters must be in a specific order
def do_thing(positional, keyword=None, *args, **kwargs):
    pass


if __name__ == '__main__':
    basket = ['cherries', 'blueberries', 'strawberries', 'gooseberries']

    get_everything(1992, 'otter', color='magenta', age=None, *basket)
