import datetime
import math
import calculations
from random import randrange

class Truck:

    def __init__(self, id, base_long, base_lat, current_long, current_lat, fk_truck_type_id, fk_transporter_id):
        self.id = id
        self.base_long = base_long
        self.base_lat = base_lat
        self.current_long = current_long
        self.current_lat = current_lat
        self.fk_truck_type_id = fk_truck_type_id
        self.fk_transporter_id = fk_transporter_id

class Job:
    def __init__(self, id, source_long, source_lat, destination_long, destination_lat, price, 
            volume, weight, fk_shipper_id, fk_preferred_truck_type_id, shipment_time, expected_delivery_time):

        self.id = id
        self.source_long = source_long
        self.source_lat = source_lat
        self.destination_long = destination_long
        self.destination_lat = destination_lat
        self.price = price
        self.volume = volume
        self.weight = weight
        self.fk_shipper_id  = fk_shipper_id
        self.fk_preferred_truck_type_id = fk_preferred_truck_type_id
        self.shipment_time = shipment_time
        self.expected_delivery_time = expected_delivery_time

    def getDistance(self):
        """
        Get source to destination distance in cartesian coordinates
        """
        return calculations.calculate_distance(self.source_long, self.source_lat, self.destination_long, self.destination_lat)

    def __lt__(self, other):
        """
        if two job have the same score, return the job with least id
        """
        return self.id < other.id

class TruckType:
    def __init__(self, id, name, volume_capacity, weight_capacity):
        self.id = id
        self.name = name
        self.volume_capacity = volume_capacity
        self.weight_capacity = weight_capacity

class Transporter:
    def __init__(self):
        self.id = id
        self.name = name

class Shipper:
    def __init__(self):
        self.id = id
        self.name = name

trucks = {}
shippers = {}
transporters = {}
jobs = {}
truckTypes = {}

trucks[1] = Truck(1, 1, 1, 5, 5, fk_truck_type_id=1, fk_transporter_id=1)
trucks[2] = Truck(2, 1, 1, 5, 5, fk_truck_type_id=2, fk_transporter_id=2)
for i in range(3, 1000):
    trucks[i] = Truck(i, randrange(1, 1000), randrange(1, 1000), randrange(1, 1000), randrange(1, 1000), randrange(1,2), randrange(1,2))


jobs[1] = Job(1, 1, 1, 4, 4, 1000, 100, 200, 1, 1, datetime.datetime.now(), datetime.datetime.now())
jobs[2] = Job(2, 1, 1, 4, 4, 1000, 100, 200, 1, 1, datetime.datetime.now(), datetime.datetime.now())
for i in range(3, 1000):
    jobs[i] = Job(i, randrange(1, 1000), randrange(1, 1000), randrange(1, 1000), randrange(1, 1000), randrange(1, 1000), randrange(1, 1000), randrange(1, 1000), 1, 1, datetime.datetime.now(), datetime.datetime.now())

truckTypes[1] = TruckType(1, "Tronton", 1000, 1000)
truckTypes[2] = TruckType(2, "CDE", 100, 100)