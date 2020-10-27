# Assume that the four inspectors at a film factory are supposed to stamp the expiration date on each
# package of film at the end of the assembly line. John, who stamps U% of the packages, fails to stamp the expiration date once in every A packages; Tom, 
# who stamps V% of the packages, fails to stamp the expiration date once in every B packages; Jeff, who stamps W% of the packages, fails to stamp the expiration 
# te once in every C packages; and Pat, who stamps X% of the packages, fails to stamp the expiration date once in every D packages. If a customer complains that
# package of film does not show the expiration date what is the probability that it was inspected by John? Use any one of the programming language 
# C/python/java/C++ to write a program to compute the probability that it was inspected by John? Display intermediate results as well as final result on the
# terminal. Further, store the same on separate output file. Program should consider only the valid run-time inputs and it should be terminated by displaying 
# an error message onto the terminal for invalid input and also the same should be stored on separate output file as similar valid test case.
# Note: This program description for four inspectors. However, program should consider “N’ number of inspectors and their name during run-time.

from collections import defaultdict
#function to caculate the probabilty
def solve(dic,person):
    numerator=dic[person][0]*dic[person][1]
    denominator=0
    for i in dic:                            #calculating using total law of probability
        denominator+=dic[i][0]*dic[i][1]
    return numerator/denominator
n=int(input("Enter number of inspectors: "))  #user input for number of inspectors
namelist=[]
for i in range(n):
    m=input("Enter name: ")                     #entering names of 'n' inspectors
    namelist.append(m)
dic=defaultdict(list)
sumofprobs=0
for i in namelist:
    per,pack=input("Enter percentage and number of packages for "+i+": ").split()       #taking input for stamping percentage and number of packages
    try:
        dic[i].append(int(per)/100)
        dic[i].append(1/int(pack))
        sumofprobs+=int(per)
    except:
        f=open("181IT231_IT302_P2_Output_TC6.txt","w")              #making sure the input for percentage and packages is an integer
        f.write("Input Value Should Be an Integer")
        f.close()
        print("Input Value Should Be an Integer")
        exit()
if(sumofprobs!=100):
    f=open("181IT231_IT302_P2_Output_TC6.txt","w")
    f.write("Sum of all the probabilities do not evaluate to 100%")     #throwing error if sum of all the probabilties is not 100
    f.close()
    print("Sum of all the probabilities do not evaluate to 100%")
    exit()
person=input("Enter name whose probability is to be checked: ")
if person not in dic:
    f=open("181IT231_IT302_P2_Output_TC6.txt","w")
    f.write("Person "+person+" is not in the list of people ")          #throwing error if wrong persons probabilty is asked 
    f.close()
    print("Person "+person+" is not in the list of people ")
else:
    ans=solve(dic,person)                                               #answer is returned and displayed
    f=open("181IT231_IT302_P2_Output_TC6.txt",'w')
    f.write("Probability that the package was inspected by "+person+" is "+str(dic[person][0])+"\n")
    f.write("Probability that the package doesnt have a expiry date given it was insepcted by "+person+" is "+str(dic[person][1])+"\n")
    f.write("Probability that a package with no expiry date has been inspected by "+person+" is "+str(ans)+"\n")
    f.close()
    print("Probability that the package was inspected by "+person+" is ",dic[person][0])
    print("Probability that the package doesnt have a expiry date given it was insepcted by "+person+" is ",dic[person][1])
    print("Probability that a package with no expiry date has been inspected by "+person+" is ",ans)