import random
import stdarray
import stdio
import sys

moves=int(sys.argv[1])
n=stdio.readInt()
stdio.readInt()
p=stdarray.create2D(n,n,0.0)
for i in range(n):
	for j in range(n):
		p[i][j]=stdio.readFloat()
hits=stdarray.create1D(n,0)
page=0
for i in range(moves):
	r=random.random()
	total=0.0
	for j in range(0,n):
		total+=p[page][j]
		if r<total:
			page=j
			break
		hits[page]+=1
for v in hits:
	stdio.writef('%8.5f',1.0*v/moves)
stdio.writeln()