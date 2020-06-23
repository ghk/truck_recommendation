import math

W1 = 1
W2 = 1
W3 = 1
W4 = 1

def calculate_distance(srcLong, srcLat, dstLong, dstLat):
        """
        Get source to destination distance in cartesian coordinates
        """
        return math.sqrt( (srcLong-dstLong) ** 2 + (srcLat - dstLat) ** 2)

def calculate_score(truck, job):
        """
        Calculate score for a pair of truck and job
        """
        score = 0
        score += W1 * calculate_distance(job.source_long, job.source_lat, truck.current_long, truck.current_lat)
        print(score)
        score += W2 * calculate_distance(job.destination_long, job.destination_lat, truck.base_long, truck.base_lat)
        print(score)
        score += W3 * job.price
        print(score)
        score += W4 * job.price / job.getDistance()
        print(score)

        return score