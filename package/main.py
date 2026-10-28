from package.add import add
from package.multiplication import multiply
# from package.evenOdd import evenOdd
import package.evenOdd as eo
import package.square as sq
print("Addition:", add(10, 20))
print("Multiplication:", multiply(10, 20))
print("evenOdd:",eo.evenOdd(10))
print("Square:",sq.square(10))