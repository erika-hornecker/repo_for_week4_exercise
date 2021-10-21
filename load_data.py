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
