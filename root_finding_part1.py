# Defining the function
def f(x):
	return (x**8) - 2

# the secant method
def secant_final(f,x0,elim,maxit):
	step = 1
	condition =True
	while condition:
		if f(x0) == f(x0 + dx):
			print('Divide by zero error!')
			break
		x2 = x0 - f(x0) * dx/ (f(x0 + dx) - f(x0))
		print('\n')
		x1 = x0 + dx
		x0 = x1
		x1 = x2
		step += 1

		if step > maxit:
			print('Not convergent')
			break
		condition = abs((x2-x0)/x2*100) > elim
		return x2, abs((x2-x0)/x2*100)

# input section
x0 = float(input('Enter first guess: '))
dx = float(input('Enter perturbation: '))
elim = float(input('Enter tolerable error: '))
maxit = int(input('Enter maximum iteration'))

solution = secant_final(f,x0,x1,elim,maxit)