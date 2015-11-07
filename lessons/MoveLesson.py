##Name: Yilin Yang
##Course: CSC 415
##Semester: Fall 2015
##Instructor: Dr. Pulimood 
##Project name: Assignment 5 - OSS Project: RoboPython
##Description: Application teaches user how to code a NAO robot in Python
##Filename: MoveLesson.py
##Description: File gives lesson on how to move NAO robot in Python
##Last modified on: 11/6/2015

##Importing modules from the Naoqi OS
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

##Constant - Robot's IP address.
##May differ depending on robot and internet connection
NAO_IP = "192.168.1.127"


##Attempt to create proxy object from ALMemory Module from Naoqi OS
try:
    memoryProxy = ALProxy("ALMemory", NAO_IP, 9559) #(Module, Robot, Robot Port)
except Exception, e:
    print "Could not create proxy to ALMemory"
    print "Error was: ", e

##Attempt to create proxy object from ALTextToSpeech Module from Naoqi OS
try:
    tts = ALProxy("ALTextToSpeech", NAO_IP, 9559) #(Module, Robot, Robot Port)
except Exception, e:
    print "Could not create proxy to ALMemory"
    print "Error was: ", e

##-----------------------------------------------------------------------------------------
##
##  Function: step1()
##
##    Parameters:    
##    
##    Pre-condition: Function is called
##
##    Post-condition: Gives first step of movement lesson
##-----------------------------------------------------------------------------------------
def step1():

    tts.say("\\rspd=75\\ Alright then, let's get started.")
    
    ##List of instructional lecture
    lecture = ["Why don't we start with the basics?",
               "To begin with, every python script will need to import the appropriate modules from the nao key O S",
               "Do you see the line printed on your terminal?",
               "First we write: from nao key import a l proxy",
               "Open up a new file and go ahead and do that."]

    ##Give speech
    ##General note - sensors only triggered if held, intention is to require one press, WIP
    for x in range(len(lecture)):
        #Skip speech
        if(memoryProxy.getData("FrontTactilTouched")): break

        #Read line from speech
        if(x == 2): print "from naoqi import ALProxy"
        tts.say("\\pau=700\\" + lecture[x])

        #Repeat previous line from speech
        if(memoryProxy.getData("RearTactilTouched")):
            if(x != 0):
                tts.say(lecture[x-1])
                tts.say(lecture[x])

        #Pause speech
        if(memoryProxy.getData("MiddleTactilTouched")):
            while(memoryProxy.getData("MiddleTactilTouched")):
                  pass

    ##Prompt to user 
    tts.say("Tap my front head sensor when you're ready to continue.")
    tts.say("Or if you'd like to hear my instructions again, tap my back head sensor.")

    ##Wait for user input
    while True:
        ##User continues
        if(memoryProxy.getData("FrontTactilTouched")):
            tts.say("Good. Moving on...")
            break

        ##User repeats   
        if(memoryProxy.getData("RearTactilTouched")):
            step1()
            break

##-----------------------------------------------------------------------------------------
##
##  Function: step2()
##
##    Parameters:    
##    
##    Pre-condition: Function is called
##
##    Post-condition: Gives second step of movement lesson
##-----------------------------------------------------------------------------------------
def step2():
    
    ##List of instructional lecture
    lecture = ["Next, we must declare an object using the modules we just imported",
               "Instantiate an object equal to an a l proxy",
               "We'll need to input several parameters as well",
               "A l proxy accepts three inputs",
               "module, \\pau=500\\ I P address, \\pau=500\\ and port number",
               "Since we're trying to code movment, we're going to use the a l motion module",
               "Your robot's I P address may vary, but port number will always be 9 5 5 9",
               "If you need to find your robot's I P address, press their chest button once"]

    ##Give speech
    ##General note - sensors only triggered if held, intention is to require one press, WIP
    for x in range(len(lecture)):
        #Skip speech
        if(memoryProxy.getData("FrontTactilTouched")): break

        #Read line from speech
        if(x == 1): print "'objectname' = ALProxy"
        if(x == 3): print "'objectname' = ALProxy(''ALMotion'', 'IP Address', 9559)"
        tts.say("\\pau=700\\" + lecture[x])

        #Repeat previous line from speech
        if(memoryProxy.getData("RearTactilTouched")):
            if(x != 0):
                tts.say(lecture[x-1])
                tts.say(lecture[x])

        #Pause speech
        if(memoryProxy.getData("MiddleTactilTouched")):
            while(memoryProxy.getData("MiddleTactilTouched")):
                  pass

    ##Prompt to user 
    tts.say("Once you've created an a l proxy object, tap my front head sensor when you're ready to continue.")
    tts.say("Or if you'd like to hear my instructions again, tap my back head sensor.")

    ##Wait for user input
    while True:
        ##User continues
        if(memoryProxy.getData("FrontTactilTouched")):
            tts.say("Good. Moving on...")
            break

        ##User repeats   
        if(memoryProxy.getData("RearTactilTouched")):
            step2()
            break

##-----------------------------------------------------------------------------------------
##
##  Function: step3()
##
##    Parameters:    
##    
##    Pre-condition: Function is called
##
##    Post-condition: Gives third step of movement lesson
##-----------------------------------------------------------------------------------------
def step3():
    
    ##List of instructional lecture
    lecture = ["Finally, all we need to do now is have our object call a method",
               "Have your a l proxy object call the move to method using the syntax shown on your terminal",
               "A l motion accepts three parameters",
               "x axis movement, \\pau=500\\ y axis movement, \\pau=500\\ and theta",
               "x and y axis movement refers to how far the robot should move in the respective direction in meters",
               "Positive x values will have the robot walk forward while negative values will have the robot walk backwards",
               "Positive y values will have the robot sidestep to the left while negative values will have the robot sidestep to the right",
               "Theta is the degree of rotation the robot will make while moving",
               "Positive theta values will have the robot rotate counter clockwise while negative values will have the robot rotate clockwise",
               "For this example, let's not have the robot run wild.",
               "We'll simply have it spin in place by inputting zero for the x and y values",
               "For theta, input 180 to have the robot rotate 180 degrees",
               "Once you're done with that, save your file and run the script",
               "Be certain that your robot has ample space to move"]

    ##Give speech
    ##General note - sensors only triggered if held, intention is to require one press, WIP
    for x in range(len(lecture)):
        #Skip speech
        if(memoryProxy.getData("FrontTactilTouched")): break

        #Read line from speech
        if(x == 1): print "'objectname'.moveTo(0.0, 0.0, 0.0)"
        tts.say("\\pau=700\\" + lecture[x])

        #Repeat previous line from speech
        if(memoryProxy.getData("RearTactilTouched")):
            if(x != 0):
                tts.say(lecture[x-1])
                tts.say(lecture[x])

        #Pause speech
        if(memoryProxy.getData("MiddleTactilTouched")):
            while(memoryProxy.getData("MiddleTactilTouched")):
                  pass

    ##Prompt to user 
    tts.say("Tap my front head sensor if you think you're done.")
    tts.say("Or if you'd like to hear my instructions again, tap my back head sensor.")

    ##Wait for user input
    while True:
        ##User continues
        if(memoryProxy.getData("FrontTactilTouched")):
            tts.say("Good. Moving on...")
            break

        ##User repeats   
        if(memoryProxy.getData("RearTactilTouched")):
            step3()
            break
        
##Used during troubleshooting, ignore please
##print "Done"

