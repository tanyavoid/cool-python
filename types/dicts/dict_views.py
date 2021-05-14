"""
Views are objects returned by dict.keys(), dict.values(), and dict.items().
"""

salad = {'potatoes': 2, 'eggs': 2, 'cucumbers': 1, 'peas': 100}

products = salad.keys()  # keys are unique, so it's a set-like object
quantities = salad.values()  # more list-like, because values are not unique
ingredients = salad.items()  # tuples of key:value pairs

# views can be iterated over
for prod, qty in ingredients:
    print(f'- {prod}: {qty} pcs')

# they support memership tests (x in view / x not in view)
'carrots' in products  # False

# they immediately (dymanically) reflect changes in a dict
salad['carrots'] = 1
'carrots' in products  # True

# can be converted to other types, list() will keep the order
list(products)
[(prod, qty) for prod, qty in ingredients]  # to create a list from pairs

# order of insertion is preverved
'carrots' in list(ingredients)[-1]  # True, 'carrots' is the last product
