# since we are going to be working with the maths module we need to import it.
import math

# Then we create the function
#as stated from the question
def gss(f,xl,xu,elim,maxit):
	#count lets us keep track of the 
	#number of iterations
	count = 1
	#condition returns True untill either we've 
	#exceeded the maximum number of iterations
	# or the error limit has been reached.
	condition = count<maxit
	
	while condition:	
		d = (xu-xl)/gr
		x1 = xl+d
		x2 = xu -d
		x0 = (x1 + x2)/2
		#print(x1,x2,count)
		e = abs((x2-x1)/x0)*100
		print('%0.5f is the approximate error for  iteration %1d '%(e,count))
		if f(x1) < f(x2):
			xl = x2
			x2 = x1
			xu =xu
			x0=x1
			count += 1
			continue
					
		elif f(x2) < f(x1):
			xu = x1
			x1 = x2
			xl =xl
			x0 = x2
			count +=1
			continue
		else:
			pass
		condition = e> elim 
		return 'Iteration number: ' + str(count),'Predicted value: ' +str(x1)


#gr is the golden ratio
gr =( 1 + math.sqrt(5))/2

#f is the function which can be substituted with any other function
f = lambda x: math.exp(x)-(5*x)

#testing the code.
a = gss(f,1,2,0.000001,40)
print(a)