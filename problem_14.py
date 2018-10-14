n=1000000

h=0
b=0
s={}
s[1] = 0
for i in range(2,n):
	j = i
	if i not in s:
		t=1
		a=i
		while(i!=1):
			if i%2==0:
				i=i/2
				t=t+1
				if i in s:
					t = t + s[i]
					break
			else:
				i=3*i+1
				t=t+1
				if i in s:
					t = t + s[i]
					break
		if t>h:
			b=a
			h=t
		s[j] = t
print b
	

