# Use any one of the programming language C/python/java/C++ to compute Sample Space S consisting of all points in the second quadrant inside a circle of 
# radius ‘r’ with center at the origin. Program should consider only positive value of ‘r’ between 75-85 during run-time. Display all computed sample points 
# on the terminal and also store the same on separate output file. Program should be terminated by 
# displaying an error message onto the terminal for invalid input and also same should be stored on separate output file as similar valid test case.
import math
def secondquadrant(radius):
    f=open("testcase6.txt","w")
    if radius<75 or radius>85:
        print("Radius of ",radius,"does not lie between 75 and 85")
        f.write("Radius of "+str(radius)+"does not lie between 75 and 85")
        f.close()
        return
    SampleSpace=[]
    f.write("sample space of coordinates within the circle of radius "+str(radius)+" are:\n")
    for i in range(0,-1*(radius+1),-1):
        for j in range(0,radius+1):
            if math.pow(i,2)+math.pow(j,2)<math.pow(radius,2):
                SampleSpace.append([i,j])
                f.write("["+str(i)+","+str(j)+"]\n")
    print("sample space of coordinates within the circle of radius ",radius," are:")
    f.close()
    for i in SampleSpace:
        print(i)

if __name__=="__main__":
    radius=input("Enter the value of your circles radius:")
    try :
        radius=int(radius)
        secondquadrant(radius)
    except:
        print(radius," is an invalid input")
        f=open("testcase6.txt","w")
        f.write(str(radius) + " is an invalid input")
        f.close()
