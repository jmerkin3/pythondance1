#beginning dance project! yewww!
from Myro import *
init("sim")

#defining all dance moves
def dancemove1(): #first move of the dance
    forward(3,.75)
    turnRight(2.49,1)
    backward(2,.75)
    
def dancemove2(): #second move of the dance
    forward(3,.75)
    turnRight(2.49,1)
    
def dancemove3(): #third move of dance
    turnLeft(5,.5)
    turnRight(5,.5)

#set up commands when music is mellow
turnRight(1,6)
turnLeft(1,6)
forward(1,3)
backward(1,4)
forward(1,2)
backward(1,1)

#dancing
for w in range(1,8):
    dancemove1()
    dancemove2()
    dancemove3()
    
#base dropping
turnLeft(1,1)
forward(2,1)
backward(2,1)
forward(1,.5)
turnRight(3,1)
turnLeft(3,1)
turnRight(.5,2)
wait(1)

#more dancing
for y in range(0,7):
    dancemove1()
    dancemove2()
    dancemove3()
    
#ending
turnBy(222)
for seconds in timer(5):
    forward(.5,1)
    print ("THE END")
print ("Thanks for Watching!")
