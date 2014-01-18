#These are how many cars there are
cars = 100
#This is how much space is in a car 
space_in_a_car = 4

#This is how many drivers there are 
drivers = 30
passengers = 90

#leftover cars 
cars_not_driven = cars - drivers

#the drivers cannot drive more than 1 car 
cars_driven = drivers

#the available space in the cars will come from the extra four seats in the cars
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "there are only", drivers, "drivers abailable."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."