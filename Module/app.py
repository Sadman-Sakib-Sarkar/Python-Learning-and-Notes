# One Way of using module and their methods
from sales import calc_shipping, calc_tax

calc_shipping()
calc_tax()



# Another Way of using module and their methods
import sales

sales.calc_shipping()
sales.calc_tax()


## default paths that python finds automatically is:
import sys
print(sys.path)


## To see all the methods of an object
print(dir(sales))

# We can also see the objects details by these magic methods:
# print(sales.__name__)
# print(sales.__package__)
# print(sales.__file__)