class Car:
    """
    A class representing a car with attributes: make, model, and year.
    """
    def __init__(self, make, model, year):
        # Initialize the attributes
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        # Print information about the car in "Year Make Model" format
        print(f"{self.year} {self.make} {self.model}")


# Create an instance of Car with the specified attributes
my_car = Car(make="Toyota", model="Corolla", year=2020)

# Call the describe_car method to print car details
my_car.describe_car()
