import time
t = time.time()
n=1000
square=2**n
s=str(square)
sum=0
for i in range(0,len(s)):
	sum=sum+int(s[i])
print sum




elapsed = time.time() - t
print 'elasped time: ' + str(elapsed)