import math as m
import struct

GR = (1 + m.sqrt(5))/2
elim = float(input("please enter error limit: "))
xl = int(input('enter the lower boundary: '))
xu = int(input('enter the upper boundary: '))
maxit = int(input('enter maximum number of iterations: '))
def gss(f,xl,xu,elim,maxit):
	
	for i in range(maxit):
		d = (xu - xl) / GR
		x1 = xl + d
		x2 = xu - d
		count = 1
		f(x1)
		f(x2)
		if f(x1) < f(x2):
			xl = x2
			x2 = x1
			x0 = x1
			e = abs(((x2 - x1)/x0) * 100)
			if e <= elim:
				maxit = 0
			else:
				continue
		elif f(x1) > f(x2):
			xu = x1
			x1 = x2
			x0 = x2
			e = abs(((x2 - x1)/x0) * 100)
			if e <= elim:
				maxit = 0
			else:
				continue
		count +=1
		xrt = x1,x2
		
		return count, xrt , e
		
		
a = gss(lambda x: m.exp(x)-(5*x),xl,xu,elim,maxit)
print(a)
