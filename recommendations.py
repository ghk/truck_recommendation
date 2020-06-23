from sanic import Sanic
from sanic.response import json
from models import jobs, trucks, truckTypes
import calculations
import queue

app = Sanic("Kargo Truck Recommendation")
NUMBER_OF_TRUCKS = 20 #Number of trucks to give recommendation for a job
NUMBER_OF_JOBS = 10 #Number of jobs to give recommendation for a truck

@app.route("/api/trucks")
async def get_trucks(request):
    return json([t.__dict__ for t in trucks])

@app.route("/api/truck-recommendations/<jobId:int>")
async def get_recommendation(request, jobId):
    job = jobs[jobId]
    pq = queue.PriorityQueue()
    for truck in trucks.values():
        truckType = truckTypes[truck.fk_truck_type_id]
        if truckType.volume_capacity >= job.volume and truckType.weight_capacity >= job.weight:
            score = calculations.calculate_score(truck, job)
            pq.put((-score, truck))
            if pq.qsize() > NUMBER_OF_TRUCKS:
                pq.get()

    results = []
    while not pq.empty():
        score, truck = pq.get()
        results.append({"truckId": truck.id, "score": -score, "transporterId": truck.fk_transporter_id})
    return json(results)

@app.route("/api/job-recommendations/<truckId:int>")
async def get_recommendation(request, truckId):
    truck = trucks[truckId]
    pq = queue.PriorityQueue()
    truckType = truckTypes[truck.fk_truck_type_id]
    for job in jobs.values():
        if truckType.volume_capacity >= job.volume and truckType.weight_capacity >= job.weight:
            score = calculations.calculate_score(truck, job)
            pq.put((-score, job))
            if pq.qsize() > NUMBER_OF_JOBS:
                pq.get()

    results = []
    while not pq.empty():
        score, job = pq.get()
        results.append({"jobId": job.id, "score": -score, "shipperId": job.fk_shipper_id})
    return json(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)