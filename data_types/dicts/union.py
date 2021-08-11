"""There are multiple ways to update and merge dictionaries in Python.
New operators for dict class offer elegant and obvious way to do it.
"""

# d1.update(d2) — d1 is updated in-place with values from d2

groceries = {'cheese': 200, 'yogurt': 400, 'oats': 400}
veggies = {'cabbage': 500, 'cucumbers': 500}

groceries.update(veggies)

# {**d1, **d2} — merge two or more dicts to a new dict

spices = {'salt': 2, 'curry': 2, 'pepper': 2}
condiments = {'mayo': 10, 'mustard': 10, 'vinegar': 10}

salad = {**veggies, **spices, **condiments}


# ------------- Union operator to easily merge and update dicts -------------

# |= — update

groceries |= veggies

# | — merge (any number of dicts) to a new dict

salad = veggies | spices | condiments
