Python script for SPEED SHOW
================
This is a small python application which detects idle time from mac os (mouse and keyboard) and forces to go to a specific website

To quit the application, just press Control+C. Else, it will continue to count the idle time

- Instead of using os.system to run the command line, I have to use os.popen to fetch the output screen

- Since I just need to get the time of second, therefore I just split the return value by '.' and then get the first bit of the array. 


idleTime.py: 
> call terminal and get the idle time from mac os 

checkinactive.py:
> This is an integrated python file: check idle time + check firefox active/inactive status + kill browser + load page with a firefox browser

It works in Mac OS X 10.5.8 + python 2.7

