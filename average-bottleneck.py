# Calculate average bottleneck value across order parameter (Xi1, Xi2)
#



import numpy as np
from scipy import stats

data = loadtxt('gluk2_bottleneck_data.dat')
Xi1 = []
Xi2 = []
Bottleneck = []
for i in range(0,len(data)):
    Xi1.append(float(data[i][0]))
for i in range(0,len(data)):
    Xi2.append(float(data[i][1]))
for i in range(0,len(data)):
    Bottleneck.append(float(data[i][2]))

binXi1 = np.arange(4.0,25.0+0.1,0.1)
binXi2 = np.arange(4.0,25.0+0.1,0.1)

ret = stats.binned_statistic_2d(Xi1,Xi2,Bottleneck,'mean',bins=[binXi1,binXi2])

gnucolumn2 = []
for i in range(0,len(np.arange(4.0,25.0,0.1))):
    gnucolumn2.append(str(np.arange(4.0,25.0,0.1)[i]))
print(gnucolumn2)

block = []
for j in range(0,len(ret.statistic)):
    gnucolumn3 = []
    for i in range(0,len(ret.statistic[j])):
        gnucolumn3.append(str(ret.statistic[j][i]))
    for i in range(0,len(gnucolumn2)):
        block.append(str(gnucolumn2[j])+" ")
        block.append(gnucolumn2[i]+" ")
        block.append(gnucolumn3[i])
        block.append("\n")
block = [w.replace('nan','0') for w in block]

gnu = open("pmf-2d-mean-gluk2.dat","w")
gnu.writelines(block)
gnu.close()

# ret.statistic and gnucolumn2 both have same dimensions (350) 


# below code generates the line space between blocks of x values
import os

infile = open('pmf-2d-mean-gluk2.dat', 'r').readlines()
output = open('pmf-2d-mean-gluk2_gp.dat', 'w')

block = infile[0].split()[0]

for x in infile:

    y = x.split()
    
    if y[0] == block:
        output.write(x)
    else:
        output.write('\n')
        output.write(x)
        block = y[0]

output.close()

os.system('mv pmf-2d-mean-gluk2_gp.dat pmf-2d-mean-gluk2.dat')
