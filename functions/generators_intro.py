"""
Generators are the way to create memory-efficient iterators.

Generator needs to be initialized, and it keeps state between calls.
All its data isn't loaded to memory all at once, and values are yielded
on demand one at a time.
"""


def infinite_integers():
    """Simple way to turn a regular function into a generator is to
    replace return statement with yield.
    """
    num = 0

    while True:
        yield num
        num += 1  # lines after yield aren't skipped


# to use the generator, we need to initialize it and assign a variable to it
nums = infinite_integers()
type(nums)  # generator
# to get values one at a time, use the next() built-in function
next(nums)  # 0
next(nums)  # 1

# another (more sugary) way to create generators — using generator expression
# huh, just like much loved list compherensions
finite_integers = (num for num in range(1000))
next(finite_integers)

# unlike generator in the first example, this one can be exhausted
