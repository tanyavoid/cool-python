"""
Sorting strings may return seemingly unexpected results.
But strings consist of characters, and numeric values — check ord() — of these
characters are compared.
list.sort() or sorted() use < comparisons, and characters of string values are
compared one by one.

Solution: specifying key=str.lower in a sorting function/method

See also: https://docs.python.org/3/howto/sorting.html
"""


def sort_strings(values):
    """Sort a list of strings with and without key parameter."""
    sorted_default = sorted(values)
    sorted_str_lower = sorted(values, key=str.lower)

    print(f'default\n{sorted(sorted_default)}')
    print(f'key=str.lower\n{sorted_str_lower}\n')


if __name__ == '__main__':
    words = ['Pear', 'orange', 'Banana', 'apple']
    sort_strings(words)

    words_ru = ['Груша', 'апельсин', 'Банан', 'Яблоко']
    sort_strings(words_ru)

    letters = ['z', 'a', 'A', 'Z']
    sort_strings(letters)
