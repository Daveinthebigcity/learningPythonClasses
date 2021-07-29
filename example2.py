""" In example 2, show the problem of trying to create multiple instances from a class """

from classFile import *

"""Imagine that this is a car hire company and I just want to create the car for the customer, but there are many customers."""

#Create the customer car
customerCar = Car('Nissan', 'Micra', 'AS22LDN', 100)

#Print the summary details
customerCar.print_vehicle_summary()


""" Here is the problem. How do I crete multiple customerCar instances without overwriting each instance. I want to be able to create a new instance each
time, that can be searchable.
So let's say that the next customer car is a Vauxhall astra....."""

#Create a second customer car
customerCar = Car('Vauxhall', 'Astra', 'DB81KER', 30000)

#Print the summary details
customerCar.print_vehicle_summary()

""" I've now re-defined customerCar and so I've overwritten the instance of the Nissan. What I want to do is be able to create repeated instances
of the car that are unique and searchable, without having to create new variables each time eg. customerCar1, customerCar2, customerCar3."""




