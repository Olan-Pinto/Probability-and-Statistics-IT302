# Use any one of the programming languages C/C++/Python/Java/R to compute Normal Approximation and Cumulative Binomial Probabilities. It should consider only 
# valid runtime inputs r=0, 1, 2, 3…, n. where ‘r’, and ‘n’ are positive integer numbers, and “p”. For invalid test case, it should display an error message on
# the terminal and the same should be stored on a separate output file with appropriate file name. For each valid test case it should display intermediate
# results as well as final output on terminal and also should store onto a separate output file in a tabular form with appropriate file name including 
# difference between both of them and also should plot graph by labeling x-axis name, y-axis name, values on x-axis, values on y-axis. Graph should be stored 
# ith appropriate file name. For each test case save the screenshot of the output with appropriate filename.
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.integrate import quad
import pandas as pd
def combinations(n,r): 				#CALCULATING nCr
	ans=1
	if(n<r):
		return 0
	if(r==0 or r==n):
		return 1
	if(n-r<r):
		r=n-r
	for i in range(1,r+1):
		ans*=(n-r+i)/i
	return ans

#CREATING Z SCORE TABLE
def normalProbabilityDensity(x):
	constant = 1.0 / np.sqrt(2*np.pi)
	return(constant * np.exp((-x**2) / 2.0) )
standard_normal_table=pd.DataFrame(data=[],index=np.round(np.arange(0,3.5,0.1),2),columns=np.round(np.arange(0.00,0.1,0.01),2))
for index in standard_normal_table.index:
	for column in standard_normal_table.columns:
		z=np.round(index+column,2)
		value, _=quad(normalProbabilityDensity,np.NINF,z)
		standard_normal_table.loc[index,column]=value
standard_normal_table.index=standard_normal_table.index.astype(str)
standard_normal_table.columns=[str(column).ljust(4,'0') for column in standard_normal_table]
#print(standard_normal_table)

f=open("181IT231_IT302_P9_Output_TC1.txt","w")
try:
	n=int(input("Enter value of n"))
	p=float(input("Enter value of p"))
except:
	print("INVALID INPUTS HENCE PROGRAM TERMINATED")
	f.write("INVALID INPUTS HENCE PROGRAM TERMINATED")
	f.close()
	exit(0)
if(n<0 or p<0 or p>1 ):
	print("INVALID INPUTS HENCE PROGRAM TERMINATED")
	f.write("INVALID INPUTS HENCE PROGRAM TERMINATED")
	f.close()
	exit(0)
f.write("INTERMEDIATE VALUES")
q=1-p
mean=n*p
sigma=math.sqrt(n*p*q)
print("mean->",mean,"standard deviation->",sigma)
f.write("\nMEAN-> "+str(mean)+" STANDARD DEVIATION-> "+str(sigma))
for i in range(n+1):
	xleft=i-0.5
	xright=i+0.5
	zleft=(xleft-mean)/sigma
	zright=(xright-mean)/sigma
	zleft_score, _=quad(normalProbabilityDensity,np.NINF,zleft)
	zright_score, _=quad(normalProbabilityDensity,np.NINF,zright)
	f.write("\nP(n<="+str(i)+")")
	print("P(n<=",i,")")
	f.write("\nCONTINUITY CORRECTION FACTOR-> "+"P("+str(xleft)+"<X<"+str(xright)+") "+"NORMAL APPROXIMATION IS-> "+ str(abs(zleft_score-zright_score)))
	print("Continuity Correction Factor: P(",xleft,"<X<",xright,")","Normal Approximation is :",abs(zleft_score-zright_score))
cumulative=0
for i in range(n+1):
	cumulative+=combinations(n,i)*pow(p,i)*pow(q,n-i)
print("Cumulative Binomial Distribution :",cumulative)
f.close()

#create range of x-values from 0 to mean+mean/2 in increments of .001
x = np.arange(0,mean*2, 0.001)

#create range of y-values that correspond to normal pdf with mean and standard deviation 
y = norm.pdf(x,mean,sigma)

#define plot 
fig, ax = plt.subplots(figsize=(9,6))
ax.plot(x,y)
ax.set_title('Normal Distribution', size = 20);
ax.set_ylabel('Probability Density', size = 20);
ax.set_xlabel('X', size = 20);
plt.grid(True, linewidth=0.5, color='#000000', linestyle='-')
#choosing plot and styling the bell curve
plt.style.use('fivethirtyeight')
plt.show()
