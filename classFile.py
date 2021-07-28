class Car():
	""" A class to define a car """

	def __init__(self, make, model, vrm, mileage):
		self.make = make
		self.model = model
		self.vrm = vrm
		self.mileage = mileage

	def print_vehicle_summary(self):
		print("Here is a quick summary of the vehicle created by the car class")
		print('Make: ' + self.make)
		print('Model: ' + self.model)
		print('Registration: ' + self.vrm)
		print(str(self.mileage) +' miles on the clock')
	
		print("**** **** **** **** **** **** **** **** ****\n")

