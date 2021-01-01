# let xi+1 be x2 and xi be x0
# Defining the function
def f(x):
	return (x*x) 

# the secant method
def secant_final(f,x0,elim,maxit):
	step = 1
	condition =True
	while condition:
		if f(x0) == f(x0 + dx):
			print('Divide by zero error!')
			break
		x2 = x0 - f(x0) * dx/ (f(x2) - f(x0))
		print('Iteratin-%d,x2 =%0.6f and f(x2) = %0.6f' % (step,x2,f(x2)))
		xrt = []
		xrt.append(x2)
	
		x0 = x1
		x1 = x2
		step += 1

		if step > maxit:
			print('Not convergent')
			break
		condition = abs((x2-x0)/x2*100) > elim
		return step,xrt, abs((x2-x0)/x2*100)

# input section
x0 = float(input('Enter first guess: '))
dx = float(input('Enter perturbation: '))
elim = float(input('Enter tolerable error: '))
maxit = int(input('Enter maximum iteration'))
x2 = x0 + dx
solution = secant_final(f,x0,elim,maxit)