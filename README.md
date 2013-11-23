Python
================
This is a small application to check the idle time in Mac OS. (Idle time refers to inactive status of mouse movement and keyboard activity)

To quit the application, just press Control+C. Else, it will continue to count the idle time

- Instead of using os.system to run the command line, I have to use os.popen to fetch the output screen

- Since I just need to get the time of second, therefore I just split the return value by '.' and then get the first bit of the array. 

