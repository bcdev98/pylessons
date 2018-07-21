import car

if __name__ == "__main__":
    my_beetle = car.Car("Volkswagen", "Beetle", 2016)
    my_telsa = car.EletricCar("Tesla", "S", 2018)
    
    my_beetle.add_fuel(10)
    my_telsa.charge()
    print(my_telsa.model)