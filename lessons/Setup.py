##Name: Yilin Yang
##Course: CSC 415
##Semester: Fall 2015
##Instructor: Dr. Pulimood 
##Project name: Assignment 5 - OSS Project: RoboPython
##Description: Application teaches user how to code a NAO robot in Python
##Filename: Setup.py
##Description: File explains application and chooses which lesson to execute
##Last modified on: 11/6/2015

##Importing modules from the Naoqi OS
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

##Importing lesson modules
import SpeechLesson
import MoveLesson

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
##  Function: initialize(ALModule)
##
##    Parameters:    
##    input ALModule; collection of Naoqi OS modules
##    
##    Pre-condition: input must be ALModule
##
##    Post-condition: Lesson type for user is selected
##-----------------------------------------------------------------------------------------
def initialize(ALModule):

    ##List of introductory speech
    talk = ["Greetings. Welcome to Python Coding for NAO.",
            "I am NAO and I will be assisting you as you write code for robots like me.",
            "You can interact with me by touching my front, middle, or back head sensors.",
            "If you want to skip some dialogue, just hold my front head sensor.",
            "If you want me to repeat what I just said, hold my back head sensor.",
            "If you need to pause this application, hold my middle head sensor.",
            "Let's start with choosing a lesson to learn about.",
            "Would you like to learn how to make me speak or how to move my joints?"]

    ##Give speech
    ##General note - sensors only triggered if held, intention is to require one press, WIP
    for x in range(len(talk)):
        #Skip speech
        if(memoryProxy.getData("FrontTactilTouched")): break

        #Read line from speech
        tts.say(talk[x])

        #Repeat previous line from speech
        if(memoryProxy.getData("RearTactilTouched")):
            if(x != 0):
                tts.say(talk[x-1])
                tts.say(talk[x])

        #Pause speech
        if(memoryProxy.getData("MiddleTactilTouched")):
            while(memoryProxy.getData("MiddleTactilTouched")):
                  pass

    ##Prompt to user  
    tts.say("Press my front head sensor for speech \\pau=500\\ or my back head sensor for movement.")

    ##Wait for user input
    while True:
        ##User selects speech lesson
        if(memoryProxy.getData("FrontTactilTouched")):
            tts.say("You've chosen speech")
            SpeechLesson.step1()
            SpeechLesson.step2()
            SpeechLesson.step3()
            break

        ##User selects movement lesson    
        if(memoryProxy.getData("RearTactilTouched")):
            tts.say("You've chosen movement")
            MoveLesson.step1()
            MoveLesson.step2()
            MoveLesson.step3()
            break

    tts.say("Wonderful! That concludes my lesson. I hope you learned something from it.")

    ##Used during troubleshooting, ignore please
    ##print "Done"
