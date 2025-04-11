class Vehicle:
    RESERVE_FUEL = 5  

    def __init__(self, mileage, fuel_left):
        self.mileage = mileage  
        self.fuel_left = fuel_left  

    def identify_distance_that_can_be_travelled(self):
        """Returns the maximum distance that can be covered without using the reserve fuel."""
        usable_fuel = self.fuel_left - self.RESERVE_FUEL
        return max(0, usable_fuel * self.mileage)

    def identify_distance_travelled(self, initial_fuel):
        """Returns the distance travelled based on initial fuel, fuel left, and mileage."""
        fuel_used = initial_fuel - self.fuel_left
        return fuel_used * self.mileage


if __name__ == "__main__":
    car = Vehicle(mileage=15, fuel_left=10)  

    print("Distance that can be travelled (without reserve fuel):",
          car.identify_distance_that_can_be_travelled(), "km")

    initial_fuel = 20  
    print("Distance travelled:", car.identify_distance_travelled(initial_fuel), "km")
