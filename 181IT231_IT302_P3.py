# Determine the value c so that each of the following function can serve as a probability distribution of the Discrete Random Variable X:
# f(x) = c × xCr × mCm-x, for x = 0, 1, 2,….n; where ‘C’ represents combination and ‘r’ and ‘m’ take only positive integer value. Use any one of the 
# programming languages C/python/java/C++ to write a program to compute the aforesaid. Program should consider only the valid run-time inputs 
# (n, r, and m values) and it should be terminated by displaying an error message onto the terminal for invalid input and also the same should be stored 
# on separate output file as similar valid test case.
def binomial_cal(n,r):   #O(min(r,n-r)) to do binomial theorem hence efficient
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

def probability_distribution(x,r,m):  			#calculating xCr * mCm-x by passing into the binomial_cal function and returning the same
	b1=binomial_cal(x,r)
	print(x,"C",r," is ",b1)
	f.write("\n"+str(x)+" C "+str(r)+" is "+str(b1))
	b2=binomial_cal(m,m-x)
	print(m,"C",m-x," is ",b2)
	f.write("\n"+str(m)+" C "+str(m-x)+" is "+str(b2))
	print(x,"C",r," * ",m,"C",m-x," is ",b1*b2)
	f.write("\n"+str(x)+" C "+str(r)+" * "+str(m)+" C "+str(m-x)+" is "+str(b1*b2))
	return b1*b2
	
n=int(input("Enter value of n: "))					 #the following 3 lines take inputs n,r,m respectively
r=int(input("Enter value of r: "))
m=int(input("Enter value of m: "))
f=open("181IT231_IT302_P3_Output_TC6.txt","w")             
f.write("Value of n is "+str(n)+"\nValue of r is "+str(r)+"\nValue of m is "+str(m))
totalprobabilty=0
for i in range(0,n+1):								#calculating totalprobability
	totalprobabilty+=probability_distribution(i,r,m)
	print("value at x=",i,"is",totalprobabilty);            
	f.write("\nValue at x= "+str(i)+" is "+str(totalprobabilty))
c=1/totalprobabilty  								#summation of f(x) from 0 to n is 1 , hence 1/totalprobability gives 'c'
print("value of c is : ",c)
f.write("\nvalue of c is : "+str(c))
f.close()