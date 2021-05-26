"""
Functions are reusable pieces of code created to do a specific task.

They are defined (created) using def keyword and giving them a name.
The name should be descriptive and short, staring with a verb, if possible.
Then a function can be called (used) any number of times to do a task.

Sometimes functions are compared to black boxes — they do some stuff, but it's
not necessary to know how it's done.
"""


def do_nothing():
    """This function does nothing."""
    pass


def return_nothing():
    """In most cases functions *return* a result. But by default it's None."""
    'Bloop'


def make_noise():
    return 'Ssssssssssssss'


def make_sound(sound='Bloop'):
    """print() doesn't replace return statement; it just has side effect.
    return must be the last line in a function; anything after that is ignored.
    """
    print(sound)
    return sound
    print('Whoosh')


if __name__ == '__main__':
    # calling (using) a function and saving its result in a variable
    nothing = return_nothing()
    assert nothing is None  # but we knew

    sound = make_sound()
    assert sound is not None
