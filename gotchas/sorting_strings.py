# list.sort() or sorted() use < comparisons between items.
# ordinals of characters in strings are compared.
# solution: specifying key=str.lower in a sorting function/method


def sort_strings(values):
    print(f'default\n{sorted(values)}')
    result = sorted(values, key=str.lower)
    print(f'key=str.lower\n{result}\n')
    return result


if __name__ == '__main__':
    words = ['Pear', 'orange', 'Banana', 'apple']
    sort_strings(words)
    words_ru = ['Груша', 'апельсин', 'Банан', 'Яблоко']
    sort_strings(words_ru)
    letters = ['z', 'a', 'A', 'Z']
    sort_strings(letters)
