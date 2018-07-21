class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self): 
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full")
    
    def add_fuel(self, amt):
        if (amt > self.fuel_capacity):
            self.fuel_level = self.fuel_capacity
        else:
            if (amt + self.fuel_level > self.fuel_capacity):
                self.fuel_level = self.fuel_capacity
                print("Fuel tank is filled up")
            else:
                self.fuel_level = amt + self.fuel_level
                print("add fuel {}".format(self.fuel_level))

    def drive(self):
        print("Drive the car")
    
# inheritance
class EletricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        # add aditional attributes
        self.battery_size = 100
        self.charge_level = 0
    
    def charge(self):
        self.charge_level = 100
        print("car is fully charged")
