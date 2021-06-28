"""
Generators are the way to create memory-efficient iterators.

Generator needs to be initialized, and it keeps state between calls.
All its data isn't loaded to memory all at once, and values are yielded
on demand, one at a time.
"""


def infinite_cookies():
    """Return cookies forever.

    yield statement in place of return turns a simple function into generator.
    In real world generators are much more useful :)
    """
    while True:
        yield 'cookie'


cookies = infinite_cookies()
type(cookies)  # generator
# fetch values using next() builtin
next(cookies)  # one at a time
next(cookies)  # cookie yet again

# another (more sugary) way to create generators — using generator expression
# huh, just like much loved list comprehensions
finite_cookies = ('cookie' for _ in range(100))
next(finite_cookies)
