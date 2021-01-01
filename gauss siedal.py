# Gauss Seidel Iteration

# Defining equations to be solved
# in diagonally dominant form A MUST for convergence
# The parameters
a11,a12,a13 =12,6,3
a21,a22,a23=3,13,2
a31,a32,a33=2,4,8
b1,b2,b3 = 171,173,84
f1 = lambda x,y,z: (b1-(a12*y)-(a13*z))/a11
f2 = lambda x,y,z: (b2-(a21*x)-(a23*z))/a22
f3 = lambda x,y,z: (b3-(a31*x)-(a32*y))/a33

# Initial setup
x0 = 0
y0 = 0
z0 = 0
count = 1

# Reading tolerable error
e = float(input('Enter tolerable error: '))

# Implementation of Gauss Seidel Iteration
print('\nCount\tx\ty\tz\n')

condition = True

while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x1,y0,z0)
    z1 = f3(x1,y1,z0)
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(count, x1,y1,z1))
    e1 = abs(x0-x1);
    e2 = abs(y0-y1);
    e3 = abs(z0-z1);
    
    count += 1
    x0 = x1
    y0 = y1
    z0 = z1
    
    condition = e1>e and e2>e and e3>e

print('\nSolution: x=%0.3f, y=%0.3f and z = %0.3f\n'% (x1,y1,z1))