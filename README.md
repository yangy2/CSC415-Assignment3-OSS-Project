# CSC415-Assignment5-OSS-Project
https://github.com/yangy2/CSC415-Assignment5-OSS-Project

Assignment 5 – Open Source Software: Project Implementation

How to Install Application:

Python files utilize Aldebaran's Naoqi OS Modules. They can be found at: https://community.aldebaran.com/en/resources/software

Program was written using IDLE Python editor on Python 2.7.10. Both can be found at: https://www.python.org/downloads

For Windows, please download Python 2.7.10. Then download the Python Naoqi SDK under the Python 2.7.10 directory.

For Mac, please download the Python Naoqi SDK and set the environment variables PYTHONPATH and DYLD_LIBRARY_PATH to /path/to/python-sdk

For Linux, please download Python 2.7.10. Then download the Python Naoqi SDK under the Python 2.7.10 directory and set the environment variable PYTHONPATH to /path/to/python-sdk

For more information on installation requirements, visit: http://doc.aldebaran.com/2-1/dev/python/install_guide.html


How to Run Application:

The application is designed to run on NAO robots. Have a NAO robot active and obtain its IP address. This can be done be pressing its chest button once. In all files under the "Lesson" folder, you will need to modify the constant "NAO_IP" to the IP address of the robot you will be using. Once done, you may run the application. It is recommended to disable Autonomous Life mode by pressing the chest button twice. Operation utilizes NAO's tactile head sensors.


Current Affairs:

-Dialogue can be skipped, paused, or repeated by holding the appropriate sensor. However, for the future, it is planned to require only a single touch to trigger.

-NAO will not recognize sensor inputs until done speaking. For the future, it is planned to allow for interrupts at any moment.

-Repeating dialogue reverts back by one line of speech and does not accept any sensor inputs while repeating the line. For the futre, possibly allow for greater callback. 

-Pausing feature, added based on user feedback, currently only works as long as button is held. Looking to remedy this inconvenience.
