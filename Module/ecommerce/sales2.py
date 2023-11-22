#this is for practicing packages.

def calc_tax():
    pass

def calc_shipping():
    pass

## module import from customer.cotact package

## Absolute Import
from ecommerce.customer import contact

contact.contact_customer()


## Relative Import
from .customer import contact #every dot means one level up of folder.

contact.contact_customer()

