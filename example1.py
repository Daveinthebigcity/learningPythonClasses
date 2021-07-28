""" In example1, create instances of a car by declaring a variable e.g. my_car, your_car and then by calling the car class """

from classFile import Car 

#Using the attributes, make, model vrm (vehicle registration mark) and mileage, generate the instance using the imported class
my_car = Car('Ford','Fiesta','DB21CAR', 500)

#Now the attributes can be accessed e.g. call the function within the class to print a summary of the car we created
my_car.print_vehicle_summary()


#To create a new instance of the class, use a new variable e.g. your_car
your_car = Car('BMW', '1 Series', 'DB22BFC', 200)

#As before, print the summary by calling a function from the class
your_car.print_vehicle_summary()

