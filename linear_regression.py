### samples
m = {1.0:3.0 , 9.0:20.0 , 5.0:14.0 , 2.0:3.0 , 7.0:11 , 6.0:12 , 14.0:30 , 19.0:40}

print m


### simulate function 
def simulate( a , b , x):	
	return a + b*x

### the init simulate value
a=1000
b=20000

### learning rate
rate=0.02


### the variation of "a" each time
def deltaA(a,b):
	d=0.0
	for key in m:
#		print "("+str(a)+"+"+str(b)+"*"+str(key)+"-"+str(m[key])+")"+"/"+str(len(m))+"="+str(simulate(a,b,key) - m[key])
		d += simulate(a,b,key) - m[key]
#	print d/len(m)
	return rate*d/len(m)

### the variation of "b" each time
def deltaB(a,b):
	d=0.0
	for key in m:
#		print "("+str(a)+"+"+str(b)+"*"+str(key)+"-"+str(m[key])+")"+"/"+str(len(m))+"="+str((simulate(a,b,key) - m[key]) * key)
		d += (simulate(a,b,key) - m[key]) * key
#	print d/len(m)
	return rate*d/len(m)	

### simplify the procedure by just setting a loop time , to check the delta value , 
### if the delta value is small enough , that means you almost get the right "a" and "b" to simulate the samples trend
for i in range(10000):
	tempa=a - deltaA(a,b)
	tempb=b - deltaB(a,b)
	print "delta value :"
	print deltaA(a,b) , deltaB(a,b)
	a = tempa
	b = tempb
	print "actual value :"
	print a , b
