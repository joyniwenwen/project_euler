n=1000
sum=0
sum1=0

s=[0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
h=[6,6,5,5,5,7,6,6]
for i in range(1,100):
	if i<21:
		sum=sum+int(s[i-1])
	elif len(str(i))==2:
		a=int(str(i)[0])
		b=int(str(i)[1])
		sum1=sum1+int(h[a-2])+int(s[b])
sum2=900*7+891*3+(sum+sum1+6)*10+11+(3+3+5+4+4+3+5+5+4)*100
print sum2
