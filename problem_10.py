import time
import math

t = time.time()

# def isprime(n):
#   for i in range(2,int(math.sqrt(n))+1):
#   	if n%i==0:
#   	  return False
#   return True

# sum=0
# h=2000000
# for j in range(2,h):
# 	if isprime(j):
# 		sum=sum+j
# print sum

n = 2000000
sum = 0
d = {}
for i in range(2, n):
	sum += i
	d[i] = True
for i in range(2, n):
	k = i
	j = i * k
	while (j < n):
		if (d[j] == True):
			sum -= j
			d[j] = False
		k += 1
		j = i * k
print sum


elapsed = time.time() - t
print 'elasped time: ' + str(elapsed)



