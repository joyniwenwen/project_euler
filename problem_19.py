num=0
h=1
for i in range(1901,2001):

	for j in range(1,13):
		if i ==2000 and j==12:
			break
		if j in [4,6,9,11]:
			length=30
		elif j==2:
			if i%4==0 and i%100!=0:
				length=29
			elif i%400==0:
				length=29
			else:
				length=28
		else:
			length=31
		h=length%7+h
		if h%7==6 :
			num=num+1
print num