from franchise import Franchise
class Simulation:

    def run_simulation(self):
        
        location_one = Franchise(1)
        location_two = Franchise(2)

        location_one.place_order()
        location_two.place_order()
        location_one.place_order()
        