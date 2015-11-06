##Name: Yilin Yang
##Course: CSC 415
##Semester: Fall 2015
##Instructor: Dr. Pulimood 
##Project name: Assignment 5 - OSS Project: RoboPython
##Description: Application teaches user how to code a NAO robot in Python
##Filename: Main.py
##Description: File runs application
##Last modified on: 11/6/2015


##Importing modules from the Naoqi OS
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

##Import Setup file
import Setup

class Main():
    ##Print welcome and instruction to user
    print "Hey! Welcome to RoboPython!"
    print "Enter 'Ctrl + C' in terminal to close application."
    ##Setup application
    Setup.initialize(ALModule)
