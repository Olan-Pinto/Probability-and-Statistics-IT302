# Implement a Graphical User Interface Binomial calculator for the following: The probability that a patient recovers from a rare blood disease is p=a. 
# If N people are known to have contracted this disease, what is the probability that exactly M survive. Use any one of the programming languages 
# C/Python/Java/C++ for implementation and it should consider only valid runtime inputs. For invalid test case, it should display an error message on the 
# appropriate place in the calculator.

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
#f=open("181IT231_IT302_P7_Output_TC1.txt","w")
error=0
try:
	p=float(input("Enter value of p: "))
except:
	print("Invalid input for p")
	error=1
#f.write("Value of p is "+str(p))
try:
	n=int(input("Enter value of N: "))
except:
	print("Invalid input for N")
	error=1
#f.write("\nValue of n is "+str(n))
try:
	m=int(input("Enter value of M: "))
except:
	print("Invalid input for M")
	error=1
if(error==1 or n<m or n<0 or m<0 or p<0 or p>1):
	print("INVALID INPUTS HENCE PROGRAM TERMINATED")
	exit(0)
#f.write("\nValue of m is "+str(m))

#BINOMIAL DISTRIBUTION FORMULA b(m;n,p)
#FORMULA IS b= nCm*p^m*q^(n-m) where q=1-p
#f.write("\n\nINTERMEDIATE VALUES\n")
print("---------------------------")
print("INTERMEDIATE VALUES")
nCm=combinations(n,m)
print("Value of nCm is",nCm)
#f.write("Value of nCm is" +str(nCm))

p_power_m=pow(p,m)
print("Value of p^m is",p_power_m)
#f.write("\nValue of p^m is " +str(p_power_m))

q=1-p
q_power_n_minus_m=pow(q,n-m)
print("Value of q^(n-m) is",q_power_n_minus_m)
#f.write("\nValue of q^(n-m) is "+str(q_power_n_minus_m))

print("---------------------------")
print("FINAL ANSWER")
#f.write("\n\nFINAL ANSWER")
print("Probability that exactly",m,"survive is ",nCm*p_power_m*q_power_n_minus_m)
#f.write("\nProbability that exactly "+str(m)+" survive is "+ str(nCm*p_power_m*q_power_n_minus_m))
#f.close()