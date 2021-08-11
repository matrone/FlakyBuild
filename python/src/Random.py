class Random:
    def __init__(self) -> None:
        self.modulus = 2147483647      
        self.multiplier = 48271
        self.default = 123456789
    
    def getNumber(self):
        seed = self.default
        Q = self.modulus/self.multiplier
        R = self.modulus%self.multiplier

        t = self.multiplier * (seed%Q) * (seed/Q)

        if t>0:
            seed = t
        else:
            seed = t + self.modulus
        
        
        return seed / self.modulus