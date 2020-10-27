# Assume that N number of ballpoint pens are selected at random from a box that contains X blue pens, Y red pens, and Z green pens. If Y is the number of 
# red pens selected and Z is the number of green pens selected, find the joint probability function f(y, z). Use any one of the programming languages 
# C/Python/Java/C++ to write a program to compute the Joint Probability Distribution and also to compute the marginal distributions of Y alone and of 
# Z alone. Program should consider only the valid run-time inputs (N, X, Y and Z positive integer values) and it should be terminated by displaying an 
# error message onto the terminal for invalid inputs and the same should be stored on a separate output file. Display all intermediate results, Joint
Probability Distribution Table and final results on terminal and also store the same on separate output file.
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
def jointprob(n, x, y, z, i, j):    #CALCULATING JOINT PROBABILITY FUNCTION
	total=x+y+z
	totalprob=combinations(total,n)
	bluecombination=combinations(x,n-i-j)
	redcombination=combinations(y,i)
	greencombination=combinations(z,j)
	return bluecombination*redcombination*greencombination/totalprob


f=open("181IT231_IT302_P4_Output_TC4.txt","w")

#TAKING INPUT FOR N,X,Y,Z
error=0
try:
	n=int(input("Enter nummber of ball point pens to be selected(N) "))
except:
	print("invalid input for N")
	error=1
try:
	x=int(input("Enter number of blue pens(X)"))
except:
	print("Invalid input for x")
	error=1
try:
	y=int(input("Enter number of red pens (Y)"))
except:
	print("Invalid input for y")
	error=1
try:
	z=int(input("Enter number of green pens(Z)"))
	
except:
	print("Invalid input for z")
	error=1
if(error==1):
	print("INVALID INPUTS HENCE PROGRAM TERMINATED")
	f.write("INVALID INPUTS HENCE PROGRAM TERMINATED")
	exit(0)
else:
	f.write("NUMBER OF BALL POINT PENS ARE "+str(n))
	f.write("\nNUMBER OF BLUE PENS ARE "+str(x))
	f.write("\nNUMBER OF RED PENS ARE "+str(y))
	f.write("\nNUMBER OF GREEN PENS ARE "+str(z))

#TO CALCULATE THE JOINT PROBABILITY OF F(Y,Z)

print("JOINT PROBABILITY DISTRIBUTION TABLE :")
f.write("\nJOINT PROBABILITY DISTRIBUTION TABLE :")
print("--------------------------------------------------------------------------------------------")
f.write("\n--------------------------------------------------------------------------------------------\n")
for j in range(-1,z):
	if(j==-1):
		print("|        |  ",end=" ")
		f.write("|        |  ")
	else:
		print(" z =  "+str(j)+"   |  ",end=" ")
		f.write(" z =  "+str(j)+"   |  ")
print("")
f.write("\n")
print("--------------------------------------------------------------------------------------------")
f.write("\n--------------------------------------------------------------------------------------------\n")
ymarginal=[]
zmarginal=[0 for i in range(z)]
for i in range(0,y+1):
	marginalfory=0
	print("|  y =",i," | ",end=" ")
	f.write("|  y = "+str(i)+"  | ")
	for j in range(0,z):
		if(i+j<=n):
			k=jointprob(n, x, y, z, i, j)
			print(k," | ",end=" ")
			f.write(str(k)+"  | ")
			marginalfory+=k
			zmarginal[j]+=k
		else:
			print("   0    | ",end=" ")
			f.write("   0    | ")
	ymarginal.append(marginalfory)
	print("")
	f.write("\n")
	print("-----------------------------------------------------------------------------------------")
	f.write("\n-----------------------------------------------------------------------------------------\n")
print("MARGINAL DISTRIBUTION FOR Y --> ",ymarginal) 					#MARGINAL DISTRIBUTION FOR Y
f.write("\nMARGINAL DISTRIBUTION FOR Y --> "+str(ymarginal))
print("MARGINAL DISTRIBUTION FOR Z -->",zmarginal)						#MARGINCAL DISTRIBUTION FOR Z
f.write("\nMARGINAL DISTRIBUTION FOR Z --> "+str(zmarginal))
print("TOTAL COMBINATIONS",combinations(x+y+z,n))
f.write("\n TOTAL COMBINATIONS "+str(combinations(x+y+z,n)))
print("FINAL ANSWER",jointprob(n, x, y, z, y, z))
f.write("\nFINAL ANSWER "+str(jointprob(n, x, y, z, y, z)))
f.close()



										





