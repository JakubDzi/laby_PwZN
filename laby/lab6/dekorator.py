from time import time
import numpy as np

def dekorator_funkc(n = 1):
    def Inner(func):
        def wrapper(*args, **kwargs):
            times=[]
            for i in range(n):
                t1 = time()
                func(*args, **kwargs)
                t2 = time()
                times.append(t2-t1)
            print("Średni czas trwania funkcji: ", np.mean(times), "s")
        return wrapper
    return Inner

def randommul(*args):
    n = args[0]
    a = np.random.random((n,n))
    b = np.random.random((n,n))
    c = np.multiply(a,b)
    #print(c)

dekorator_funkc(10)(randommul)(5000)