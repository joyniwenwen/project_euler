fib=[1,1]
fib_new=0
i=2
while(len(str(fib_new))<1000):
	fib_new=fib[i-2]+fib[i-1]
	fib.append(fib_new)
	i=i+1
print i
