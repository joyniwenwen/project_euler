items = [0,1,2,3,4,5,6,7,8,9 ]
s=[]
from itertools import permutations
for p in permutations(items):
	s.append(p)
print(s[999999])
