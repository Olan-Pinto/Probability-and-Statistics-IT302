# Assume that the weights of bags of chips for a vending machine are normally distributed with a mean of “A” ounces and a standard deviation of “B” ounce. Bags 
# hat have weights in the lower C% are too light and will not work in the machine. Use any one of the programming languages C/C++/Python/Java/R to compute what 
# is the least a bag of chips can weigh and still work in the machine? Program should consider only the valid runtime positive integer/real numbers as inputs.
#  For invalid test case, it should display an error message on the terminal and the same should be stored on a separate output file with appropriate file name. 
#  For each valid test case it should display intermediate result as well as final output on terminal and also should store onto a separate output file with 
#  appropriate file name. Furthermore, it should plot Normal Distribution Curve with label by shading the appropriate area on the curve and the graph should be 
#  saved with appropriate file name. For each test case save the screenshot of the output with appropriate filename.
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import stats as stats
from scipy.stats import norm
f=open("181IT231_IT302_P10_Output_TC6.txt","w")
try:
	a=float(input("Enter value of A : "))
	b=float(input("Enter value of B : "))
	c=str(input("Enter value of C : "))
except:
	print("INVALID INPUTS HENCE PROGRAM TERMINATED")
	f.write("INVALID INPUTS HENCE PROGRAM TERMINATED")
	f.close()
	exit(0)
c=float(c[0])
c=c/100
if(a<0 or b<0 or c<0 ):
	print("INVALID INPUTS HENCE PROGRAM TERMINATED")
	f.write("INVALID INPUTS HENCE PROGRAM TERMINATED")
	f.close()
	exit(0)
f.write("INTERMEDIATE VALUES")
zscore=scipy.stats.norm.ppf(c)
print("zscore =",zscore)
f.write("\nZSCORE-> "+str(zscore))
x=a+zscore*b
print("μ + zσ =",x)
f.write("\nmiu + z*sigma-> "+str(x))
f.close()
#to plot graph
plt.style.use('ggplot')
mean=a
std=b
xg=np.linspace(0, mean*2,1000)
iq=stats.norm(mean,std)
plt.plot(xg,iq.pdf(xg),'b')
px=np.arange(0,x,0.01)
plt.fill_between(px,iq.pdf(px),color='r')
plt.show()

