from vpython import *

#Python code for simple integration using Monte Carlo method

#Define constants
x_coord=0.0                          #x co-ordinate of stone
y_coord=0.0                          #y co-ordinate of stone 
maxit=1000                           #number of stones thrown
x_min=-1                             #lower limit of x integral
x_max=3                              #upper limit of x integral
accepted_value=28/3                  #accepted value of the integral

#Define variables
meas_int=0.0                         #variable holding the mesaured integral
incount=0                            #variable to count splashes
M=1                                  #number of times for each N is repeated 
MInt=0                               #holds the sum of the integral values for specific N 
averageInt=0                         #average integral value for the M times 
i=0.0                                #inner loop variable
j=0                                  #outer loop variable
integral=0.0                         #variable to hold the MVT integral value 
x1=0.0                               #variable to get random MVT x value
y1=0.0                               #variable to get random MVT y value

# Define the function to integrate
def f(x):
    return x**2

  
#Define graphical displays
gdisplay()                                      #define display for stones
inside1=gdots(color=color.red)                  #colour for splashes (inside)
outside1=gdots(color=color.blue)                #colour of the stones outside

gdisplay()                                      #define display for stones
inside2=gdots(color=color.red)                  #colour for splashes (inside)
outside2=gdots(color=color.blue)                #colour of the stones outside

gdisplay()                                      #define display for graph
plotintegral=gdots(color=color.black)

gdisplay()                                      #define display for graph
plotmeanintegral=gdots(color=color.green)



#PROCESSING

#Stone Throwing Approach
#loop over M times
for j in range(1,M+1):                         
#reset of variables
    i=0                                        #resetting inner loop variable
    incount=0                                  #resetting splashes count
    meas_int=0                                 #resetting variable holding the value of the integral
    #delete graph contents
    outside1.delete()
    inside1.delete()
    #Throw N stones
    for i in range(1,maxit+1):                                                 #loop runs maxit times
        rate(100)                                                              #how fast or slow visualisation is 
        #Throw a stone
        x_coord=x_min+random(x_max-x_min)                                      #gets the x-coordinate of the throwing stone
        y_coord=random(0, f(x_min),f(x_max))                                   #gets the y-coordinate of the throwing stone
        #Check whether stone splashed or not
        if y_coord<=(f(x_coord)):
            incount=incount+1                                                  #counting and holding splashes
            inside1.plot(pos=(x_coord,y_coord))                                #plot stone in red
        else:                                                                  #stone is blue if outside  
            outside1.plot(pos=(x_coord,y_coord))
        #Determine the measured integral
        meas_int= (x_max-x_min)*max(f(x_min),f(x_max))*(incount/maxit)         #formula to get the integral
        #Plot current value of integral 
        plotintegral.plot(pos=(i, meas_int))                                   #plots the N vs calculated value
    MInt=MInt+meas_int                                                         #holds M values of integral

averageInt=(MInt/M)                                                            #average integral value


#Mean Value Theorem Approach
for j in range(1,M+1):                         
#reset of variables
    i=0                                        #resetting inner loop variable
    incount=0                                  #resetting splashes count
    integral=0                                 #resetting variable holding the value of the integral
    #delete graph contents
    outside2.delete()
    inside2.delete()
    #loop over maxit amount of times
    for i in range(1, maxit+1):
        rate(100)
        x1=x_min+random()*(x_max-x_min)                                        #formula to get a random x value 
        y1=random(0, f(x_min),f(x_max))
        integral=integral+f(x1)                                                #formula to get the integral value
        if y1<=(f(x1)):
            incount=incount+1                                                  #counting and holding splashes
            inside2.plot(pos=(x1,y1))                                          #plot inside stone in red
        else:                                                                  #stone is blue if outside  
            outside2.plot(pos=(x1,y1))
        plotmeanintegral.plot(pos=(i, (x_max-x_min)/maxit*integral))           #plots N vs calculated value
    
mean_val=(x_max-x_min)/maxit*integral                                          #integral value for MVT



#OUTPUT

print("Integration estimate using stone approach = ",averageInt)                     #prints integral gotten through stone throwing approach Monte Carlo method 
aberror1 = abs(accepted_value-averageInt)                                            #absolute error of stone throwing approach
print("Absolute error = ",aberror1)                                                  #prints absolute error

print("Integration estimate using the mean value theorem approach: ",mean_val)           #prints integral gotten through the mean value theorem Monte Carlo method 
aberror2 = abs(accepted_value-mean_val)                                                  #absolute error of mean value theorem approach
print("Absolute error = ",aberror2)                                                      #prints absolute error
