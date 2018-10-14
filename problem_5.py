import time
from math import sqrt 

t = time.time()
n=10

s=[]
result = 1
for i in range(1,n+1):
  s.append(i)
for i in range(0,n):
	for j in range(i+1,n):
		if s[j] % s[i] == 0:
			s[j] = s[j] / s[i]
	result = result * s[i]

print result




elapsed = time.time() - t
print 'elasped time: ' + str(elapsed)
