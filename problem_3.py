import math

def isprime(n):
  for i in range(2,int(math.sqrt(n))+1):
  	if n%i==0:
  	  return False
  return True

num=600851475143
index=1
while(index<=num):
  if isprime(index) and num%index==0:
  	num/=index
  	maxprime=index
  index+=1
print maxprime