import stdarray
import stdio
import sys
moves=int(sys.argv[1])
n=stdio.readInt()
stdio.readInt()
probs=stdarray.create2D(n,n,0.0)
for i in range(n):
	for j in range(n):
		probs[i][j]=stdio.readFloat()
ranks=stdarray.create1D(n,0.0)
ranks[0]=1.0
for i in range(moves):
	newRanks=stdarray.create1D(n,0.0)
	for j in range(n):
		for k in range(n):
			newRanks[j]+=ranks[k]*probs[k][j]
		ranks=newRanks
for rank in ranks:
	stdio.writef('%8.5f',rank)
stdio.writeln()

