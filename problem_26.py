l=[]
h=[]
for i in range (2,1000):
		a=10**(len(str(i)))
		e=a/10
		s=[e]
		j=i
		j=a%j
		while(j not in s): 
			s.append(j)
			j=(j*10)%i
			
		d=s.index(j)
		n=len(s)-d
		l.append(n)
		h.append(i)
num=0
for i in range(0,len(l)):
	num=max(l[i],num)
c=l.index(num)
b=h[c]
print b
