import math

def isprime(n):
  for i in range(2,int(math.sqrt(n))+1):
  	if n%i==0:
  	  return False
  return True

s=0
index=2
while(s<10001):
	if isprime(index):
		s=s+1
	index=index+1
print index-1
