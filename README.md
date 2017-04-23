# Python script for SPEED SHOW
This is a small python script that detects idle time from mac os (mouse and keyboard), and then it forces the computer visits a specific website with Firefox

# Operations
To quit the application, just press Control+C. Else, it will continue to count the idle time

- Instead of using os.system to run the command line, I have to use os.popen to fetch the output screen(it is a perl command)

- Since I just need to get the time in 'second', I just split the return value by '.' and then get the first bit of the array to roughly indicate as the idle time in second

# Two scripts
idleTime.py: 
> call terminal and get the idle time from mac os 

checkinactive.py:
> This is an integrated python file: check idle time + check firefox active/inactive status + kill browser + load page with a firefox browser

# Tested configuration
It works in Mac OS X 10.5.8 + python 2.7

