import numpy as np 
import matplotlib.pyplot as plt 
import sympy # for evaluating number of primes <= n 

def f(n):
	arr = []
	for i in range(1,n+1):
		arr.append(sympy.primepi(i))
		#print('For',i, 'value', arr[i-1])
	return arr

ar = f(100)

t1 = np.arange(1,101,1,dtype = int)
plt.step(t1, ar ,'b-')
plt.axis([0,110,0,25]) 
plt.show()  














