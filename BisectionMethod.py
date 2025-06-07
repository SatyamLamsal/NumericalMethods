class BisectionMethod:
    def __init__(self, a, b, c, rn1, rn2,toleration):
        self.a = a
        self.b = b 
        self.c = c 
        self.range_1 = rn1
        self.range_2 = rn2
        self.numberofiterations = 1000
        self.tempc = 0
        self.root = -1
        self.tolerance = toleration
        
    def FunctionVal(self, x):
        return (self.a*(x**2) + self.b * x + self.c)
    
    def CalculateRootIteratively(self):
        if ((self.FunctionVal(self.range_1) * self.FunctionVal(self.range_2)) > 0):
            return False

        while (self.numberofiterations>0):            
            self.tempc = (self.range_1 + self.range_2) / 2
            if((self.tempc*self.a)>0):
                self.a = self.tempc 
            else:
                self.b = self.tempc    
            self.numberofiterations -= 1                  
        self.root = self.tempc
        return True
    
    def displayroot(self):
        print(f"Positive Root of Polynomial is : {self.root:.4f}")


# y = x^2 -5x + 6

BisecVar = BisectionMethod(1, -5, 6, 1.5, 2.5,0.0001)
if BisecVar.CalculateRootIteratively():
    BisecVar.displayroot()