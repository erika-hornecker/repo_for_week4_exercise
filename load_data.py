import numpy as np
import pandas as pd

# In this file, you'll put all the functions for creating the Fibonacci sequence up to a certain number.

def fibm(n):
	fibm = []
	def fib(n):
		if n < 2:
			return n
		else:
			return fib(n-1) + fib(n-2)
	for i in range(n):
		fibm.append(fib(i))

def Fib_seq(nmax:float) -> list:
    """
    creating the Fibonacci sequence up to nmax

    Parameters
    ----------
    nmax : float
        upeer bound of the sequence

    Returns
    -------
    list
        Fibonacci sequence

    """
    
    res = [0,1]
    
    i = 0
    while res[i] + res[i+1] <= nmax:
        res.append(res[i] + res[i+1])
        i += 1
        
    return res

