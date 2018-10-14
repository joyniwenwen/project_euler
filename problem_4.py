import time

t = time.time()
def isPalindrome(n):
	number=[]
	while(n != 0):
		a=n%10
		number.append(a)
		n=n/10
	b=len(number)
	for i in range (0,b/2):
	  if number[i]!= number[b-1-i]:
	  	return False
	return True

# n = raw_input("number: ")
# if isPalindrome(int(n)):
# 	print 'ok'
# else:
# 	print 'not ok'
z=0
for x in range(100,1000):
	for y in range(100,1000):
	  if isPalindrome(y*x):
	  	z=max(z,y*x)
print z

elapsed = time.time() - t
print 'elasped time: ' + str(elapsed)
