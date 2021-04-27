# https://docs.python.org/3/tutorial/floatingpoint.html
# "most decimal fractions cannot be represented exactly as binary fractions"

from decimal import Decimal

print(f'0.1 * 3\n>>> {0.1 * 3}')
print(f'0.1 * 3 == 0.3\n>>> {0.1 * 3 == 0.3}')

# decimal module provides the exact decimal representation
# suitable when high precision is required
d = Decimal(0.1)
print(f'Decimal(0.1)\n>>> {d}')

# a simpler solution is to use integers (like cents or milliseconds)
