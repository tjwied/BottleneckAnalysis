import numpy
from numpy import *
bottleneck = loadtxt('pmf-2d-mean-gluk2.dat')
opendata = []
closeddata = []

Po = 0
Pc = 0
kBT = 0.001987191 * 300
pmf = loadtxt('pmf-2d_gp_apo.dat')
for i in range(60, 230):
	Po = 0
	Pc = 0
	distance = i * 0.1
	for i in range(0, len(pmf)):
		if 0 < bottleneck[i][2] < distance:
        		if pmf[i][0] == bottleneck[i][0] and pmf[i][1] == bottleneck[i][1]:
                       		Pc += math.exp(-pmf[i][2]/(kBT))
		if bottleneck[i][2] >= distance:
        		if pmf[i][0] == bottleneck[i][0] and pmf[i][1] == bottleneck[i][1]:
                		Po += math.exp(-pmf[i][2]/(kBT))
			
	#print Po/Pc
	dG = -kBT*(numpy.log(Po/Pc))
	print distance, dG

