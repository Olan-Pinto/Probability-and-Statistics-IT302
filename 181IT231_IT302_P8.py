# Lots of “A” number of components each are deemed unacceptable if they contain “≥B” number of defectives. The procedure for sampling a lot is to select 
# “C” number of components at random and to reject the lot if a defective is found. Compute the probability that exactly “D” number of defective is found in
# the sample if there are “B” number of defectives in the entire lot using any one of the programming languages C/C++/Python/Java/R. Computer mean and variance
# of the random variable, and then use Chebyshev’s theorem to interpret the interval μ ± 2σ. Program should consider only valid runtime inputs. For invalid test
# case, it should display an error message on the terminal and the same should be stored on a separate output file with appropriate file name. For each valid
# test case it should display intermediate results as well as final output on terminal and also should store onto a separate output file with appropriate file 
# name. For each test case save the screenshot of the output with appropriate filename.
import math
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
f=open("181IT231_IT302_P8_Output_TC6.txt","w")
a=int(input("Enter value of A : "))
b=int(input("Enter value of B : "))
c=int(input("Enter value of C : "))
d=int(input("Enter value of D : "))
if(a<0 or b<0 or c<0 or d<0):
	print("INVALID INPUTS HENCE PROGRAM TERMINATED")
	f.write("INVALID INPUTS HENCE PROGRAM TERMINATED")
	f.close()
	exit(0)
f.write("INTERMEDIATE VALUES")
one=combinations(b,d)
two=combinations(a-b,c-d)
three=combinations(a,c)
prob=(one*two)/three
print("probabilty of",d,"component/s to be defective is/are : ",prob)
f.write("\nprobabilty of "+str(d)+" component/s to be defective is/are : "+str(prob))
mean=b*c/a
print("mean->",mean)
f.write("\nMEAN->"+str(mean))
variance=((a-c)/(a-1))*c*(b/a)*(1-(b/a))
print("variance->",variance)
f.write("\nVARIANCE->"+str(variance))
standard_deviation=math.sqrt(variance)
print("standard deviation->",standard_deviation)
f.write("\nSTANDARD DEVIATION->"+str(standard_deviation))
left=mean - 2*standard_deviation
#left=0 if mean - 2*standard_deviation<0 else mean - 2*standard_deviation
right=mean+2*standard_deviation
print("Chebyshev's interval for μ ± 2σ is : (",left,",",right,")")
f.write("\nChebyshev's interval : ( "+str(left)+" , "+str(right)+" ) ")
f.close()
