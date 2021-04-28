"""
"most decimal fractions cannot be represented exactly as binary fractions"
https://docs.python.org/3/tutorial/floatingpoint.html
"""

from decimal import Decimal

print('>>> 0.1 * 3')
print(0.1 * 3)
print('>>> 0.1 * 3 == 0.3')
print(0.1 * 3 == 0.3)

# decimal module provides the exact decimal representation
# suitable when high precision is required
d = Decimal(0.1)
print('>>> Decimal(0.1)')
print(d)
