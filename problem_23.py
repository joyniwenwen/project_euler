import math
import time

t = time.time()

# def sumofdivisors(n):
# 	sum=1
	
# 	for i in range(2,int(n**0.5)+1):
# 		if i**2==n:
# 			sum=sum+i
# 		elif n%i==0 :
# 			sum=sum+i+n/i
# 	return sum

# def abundantnumber(n):
# 	if sumofdivisors(n)>n:
# 		return True

# dic={}
# s=[]
# h=[]
# sum=0
# for i in range(12,28112):
# 	if abundantnumber(i):
# 		s.append(i)


# for i in range(0,len(s)):
# 	for j in range(i,len(s)):
# 		if s[i]+s[j]>28123:
# 			break
# 		elif dic.get(s[i]+s[j])==None: 
# 			h.append(s[i]+s[j])
# 			dic[s[i]+s[j]]=True
# for i in range(0,len(h)):
# 	sum=sum+h[i]
# sum=(1+28123)*28123/2-sum

# elapsed = time.time() - t
# print 'elasped time: ' + str(elapsed)


# divisor_sum_list = []
# n = 28123
# for i in range(0, n+1):
# 	divisor_sum_list.append(0)
# for i in range(1, n/2 + 1):
# 	k = 2
# 	while ( i * k <= n):
# 		divisor_sum_list[i * k] += i
# 		k += 1

# abundant_number_list = []
# for i in range(1, n + 1):
# 	if divisor_sum_list[i] > i:
# 		abundant_number_list.append(i)

# dic = {}
# for i in abundant_number_list:
# 	for j in abundant_number_list:
# 		if i+j < n:
# 			dic[i + j] = True


# sum = 0
# for i in range(1, n):
# 	if dic.get(i) == None:
# 		sum += i
# print sum

def abun(N):
    Q = dict.fromkeys(range(1,N+1), 0)
    for q in Q:
        for k in [q*n for n in range(1,N//q+1) ]:
            if q!=k: Q[k] += q
    return [ q  for q in Q if Q[q]>q]

N = 20161; A = abun(N); possible = set() 
for a in A:
    for b in A:
        if a+b < N: possible.add( a+b )
        else: break

print (sum([p for p in range(N) if p not in possible]))

elapsed = time.time() - t
print 'elasped time: ' + str(elapsed)

			
