import numpy as np

class BisectionMethod:
    def __init__(self, a, b, c,ran_a, ran_b):
        self.a = a
        self.b = b 
        self.c = c 
        self.range_1 = ran_a
        self.range_2 = ran_b
        self.numberofiterations = 100
        self.tempc = 0
        self.root = -1
        
    def FunctionVal(self, x):
        return (self.a*(x**2) + self.b * x + self.c)
    
    def CalculateRootIteratively(self):
        if((self.FunctionVal(self.range_1)) > 0 ):
            return False

        while ( self.numberofiterations > 0):
            self.tempc = (self.range_1 + self.range_2) / 2 
            if((self.FunctionVal(self.tempc)>0) and (self.FunctionVal(self.range_1)<0)):
                self.range_2 = self.tempc 
            else:
                self.range_1 = self.tempc 

            self.numberofiterations -= 1      
        self.root = self.tempc
        return True
    
    def displayroot(self):
        print(f"Positive Root of Polynomial is : {self.root:.4f}")


# y = x^2 -5x + 6
BisecVar = BisectionMethod(1, -5, 6, 2, 4)
BisecVar.CalculateRootIteratively()
BisecVar.displayroot()