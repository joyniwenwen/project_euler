sum1=0
sum2=0
for i in range(1,101):
	sum1=sum1+i**2
for j in range(1,101):
	sum2=sum2+j
sum3=sum2**2
print sum3-sum1
