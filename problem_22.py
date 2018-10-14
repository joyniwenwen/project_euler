file_name = 'p022_names.txt'
data = []
for line in open(file_name):
    line = line.split()
    data.append(line)
a=data[0][0]
a=a.replace('"','')
a=a.split(',')
a.sort()
h=0
for i in range(0,len(a)):
	sum=0
	for j in range(0,len(a[i])):
		sum=sum+ord(a[i][j])-ord('A')+1
	product=sum*(i+1)
	h=h+product
print h

