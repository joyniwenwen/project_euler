for a in range(0,1001):
	for b in range(a,1001-a):
		c=1000-a-b
		if a**2+b**2==c**2 and c>b:
			print a*b*c,a,b,c