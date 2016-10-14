#beginning dance project! yewww!
from Myro import *
init("sim")

#defining all dance moves
def move1(): #first move of the dance
    forward(3,1)
    
def move2(): #second move of the dance
    wait(.5)
    turnRight(3,1)
    
def move3(): #third move of dance
    wait(1)

#until base drop, run this x number of times
#try to sync end of this up with base drop
for w in range(1,18):
    move1()
    move2()
    move3()

#movement commands for base drop and maybe initsim
#stuff

#go back to loop or make new loop
for y in range(0,5):
    move1()


