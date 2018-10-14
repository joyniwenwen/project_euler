import math
n=0

step=1
h=1
while(h<=250):
	h=0
	n=n+step
	step=step+1
	for i in range(1,int(math.sqrt(n))+1):
		if n%i==0:
			h=h+1
print n