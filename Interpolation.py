import numpy as np

def Create2DMapping(OneDArray):
    Map = np.zeros(2*(len(OneDArray)-1))
    Map.resize(len(OneDArray),len(OneDArray))
    cache = 0
    
    for j in range(0, len(OneDArray)-1):
        for i in range(0,len(OneDArray)-1):
            cache = OneDArray[i] - OneDArray[i+1]
            if(cache<0):
                cache *= -1
            Map[i][j] = cache
            
        for k in range(0, len(OneDArray)-1):
            OneDArray[k]=Map[k][j]
    return Map






data= np.array([1,3,6,10,15])
print(Create2DMapping(data))

