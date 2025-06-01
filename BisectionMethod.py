import numpy as np



class BisectionMethod:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b 
        self.c = c 
        self.range_1 = 6
        self.range_2 = 7
        self.numberofiterations = 10
        self.tempc = 0
        self.root = -1
        
    def FunctionVal(self, x):
        return (self.a*(x**2) + self.b * x + self.c)
    
    def CalculateRootIteratively(self):
        if((self.FunctionVal(self.range_1)) > 0 ):
            return False;

        while ( self.numberofiterations > 0):
            self.tempc = (self.range_1 + self.range_2) / 2;
            if((self.FunctionVal(self.tempc)>0) and (self.FunctionVal(self.range_1)<0)):
                self.range_2 = self.tempc;
            else:
                self.range_1 = self.tempc;

            self.numberofiterations -= 1
        
        self.root = self.tempc
        return True
    
    def displayroot(self):
        print(f"Positive Root of Polynomial is : {self.root:.4f}");
                
            
a = 1
b = -7
c = 2


print('Hello World!')



SqFxn = BisectionMethod(a,b,c) 
SqFxn.CalculateRootIteratively()
SqFxn.displayroot()
