import datetime
from models import Job, Truck
import math
import calculations

def testDistance():
    job = Job(1, 1, 1, 4, 4, 1000, 
            100, 200, 1, 1, datetime.datetime.now(), datetime.datetime.now())
    assert job.getDistance() == math.sqrt(18)

def testScore():
    job = Job(1, 1, 1, 4, 4, 1000, 
            100, 200, 1, 1, datetime.datetime.now(), datetime.datetime.now())
    truck = Truck(1, 1, 1, 5, 5, fk_truck_type_id=3, fk_transporter_id=1)
    result = math.sqrt(32) + math.sqrt(18) + 1000 + (1000 / math.sqrt(18))
    score = calculations.calculate_score(truck, job) 
    assert score == result


