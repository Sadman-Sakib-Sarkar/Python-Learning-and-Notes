## Importing packages from other folder

## One Way:
import ecommerce.sales2

## Accessing methods:
ecommerce.sales2.calc_shipping()
ecommerce.sales2.calc_tax()


## Another Way:
from ecommerce.sales2 import calc_shipping, calc_tax

## Accessing methods:
calc_tax()
calc_tax()

## For accessing as an object (Third Way)
from ecommerce import sales2

sales2.calc_shipping()
sales2.calc_tax()
