"""
Functions are useful reusable pieces of code created to do a specific task.

They are defined (created) using *def* keyword following by a name.
The name should be descriptive and short, starting with a verb, if possible.
Then a function can be called (used) any number of times to do its task.

Sometimes functions are compared to black boxes — they do their thing, but it's
not necessary to know how it's done.
"""


def do_nothing():
    """This function does nothing, meh."""


def return_nothing():
    """In most cases functions *return* a result. But by default it's None."""
    print('Doin some stuff but return nothing.')


def make_noise():
    return 'Ssssssssssssss'


def make_sound(sound='Bloop'):
    """print() doesn't replace return statement; it just has a side effect.
    return must be the last line in a function; anything after that is ignored.
    """
    print(sound)
    return sound
    print('Whoosh')  # unreachable


if __name__ == '__main__':
    # calling a function and saving its result in a variable
    nothing = return_nothing()
    assert nothing is None

    noise = make_noise()
    assert noise is not None

    sound = make_sound()
    assert sound is not None
