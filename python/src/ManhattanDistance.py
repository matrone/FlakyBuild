from Geometry import Geometry
from math import fabs


class ManhattanDistance(Geometry):

    def calculate_distance(self, vector: list, points: list) -> float:
        distance: float = 0
        for i in range(1, super().problem_size):
            abs_sum = fabs(vector[i] - points[i])
            distance += abs_sum

        return distance
