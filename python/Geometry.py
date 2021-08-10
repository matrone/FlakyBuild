import math

class Geometry:
    
    def __init__(self, problemSize):
        self.problemSize = problemSize
    
    def euclideanDistance(vector, points):
        sum = 0
        for i in range(0,self.problemSize,1):
            tmp = vector[i] - points[i]
            sum += tmp*tmp
        return math.sqrt(sum)

    def matches(vector, dataset, minDist):
        pass
