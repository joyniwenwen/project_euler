def sumofdivisors(n):
	sum=1
	
	for i in range(2,int(n**0.5)+1):
		if i**2==n:
			sum=sum+i
		elif n%i==0 :
			sum=sum+i+n/i

	return sum
s=[]
sum=0
for i in range(1,10000):
	if i in s:
		sum=sum
	elif i==sumofdivisors(sumofdivisors(i)) and i!=sumofdivisors(i):
		s.append(i)
		s.append(sumofdivisors(i))
		sum=sum+i+sumofdivisors(i)
print sum

