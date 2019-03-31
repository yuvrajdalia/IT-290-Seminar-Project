import stdarray
import stdio
n=stdio.readInt()
links=stdarray.create2D(n,n,0)
outLinks=stdarray.create1D(n,0)
while not stdio.isEmpty():
	i=stdio.readInt()
	j=stdio.readInt()
	outLinks[i]+=1
	links[i][j]+=1
stdio.writeln(str(n)+' '+str(n))
for i in range(n):
	for j in range(n):
		p=(.90*links[i][j]/outLinks[i])+(.10/n)
		stdio.writef('%8.5f',p)
	stdio.writeln()