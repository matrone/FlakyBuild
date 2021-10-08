from Distance import Distance
import math


class EuclideanDistance(Distance):

    def calculate(self, vector: list, points: list) -> float:
        distance: float = 0
        for i in range(self.problem_size):
            tmp = vector[i] - points[i]
            distance += tmp * tmp

        return math.sqrt(distance)
