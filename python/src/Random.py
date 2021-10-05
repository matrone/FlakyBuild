class Random:
    def __init__(self) -> None:
        self.modulus = 2147483647      
        self.multiplier = 48271
        self.seed = 123456789
    
    def getNumber(self):
        Q = self.modulus / self.multiplier
        R = self.modulus % self.multiplier

        t = self.multiplier * (self.seed % Q) - R * (self.seed / Q)

        if t > 0:
            self.seed = t
        else:
            self.seed = t + self.modulus
        
        
        return float(self.seed / self.modulus)
