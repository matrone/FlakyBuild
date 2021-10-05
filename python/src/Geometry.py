import math

class Geometry:

    def __init__(self, problemSize):
        self._problemSize = problemSize

    @property
    def problemSize(self):
        return self._problemSize

    @problemSize.setter
    def problemSize(self, problemSize):
        self._problemSize = problemSize

    def euclideanDistance(self, vector, points):
        sum = 0
        for i in range(self.problemSize):
            tmp = vector[i] - points[i]
            sum += tmp * tmp
        return math.sqrt(sum)

    def matches(self, vector, dataset, minDist):
        for it in dataset:
            dist = self.euclideanDistance(vector, it)
            if dist <= minDist:
                return True
        return False