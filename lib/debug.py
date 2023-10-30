#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee 

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    c1 = Customer("Emiley")
    c2 = Customer("Adam")
    coffee1 = Coffee("Mocha")
    coffee2 = Coffee("Latte")
    order1 = Order(c1, coffee1, 5.0)
    order2 = Order(c1, coffee1, 5.0)
    order3 = Order(c1, coffee2, 1.0)

    ipdb.set_trace()
