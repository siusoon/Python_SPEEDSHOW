# logic: detect idle time and force browser's hp reset

import sys,os,time
import webbrowser

# define variable
sleeptime = 5  #how frequent to get the idle time
temp_idle_value = 6  #Duration to reset browser (in sec format)

def main_loop():
    while 1:
		#cmd = "ps axo pid,command | grep '[P]rocessing'"
		#os.system()
		time.sleep(sleeptime)
		cmd = "ioreg -c IOHIDSystem | perl -ane 'if (/Idle/) {$idle=(pop @F)/1000000000; print $idle}'"
		result = os.popen(cmd)
		str = result.read()
		temp_idle = int(str.split(".")[0])
		
  		if temp_idle > temp_idle_value and status == 0:
  			resetBrowser()
  			status = 1
  			
  		elif temp_idle > temp_idle_value and status == 1:
  			print("do nothing")
  			
  		else:
  			print("continue")
  			status = 0

def resetBrowser():
	print(os.system("ps axo pid,command | grep '[P]rocessing'"))  #256 means not active, else will display a whole line
	print("idle time, do something, force browser quit and load webpage")
  		
if __name__ == '__main__':
    
    try:
        status = 0
        main_loop()
    except KeyboardInterrupt:  #control+c in mac
   		print ('stop')
    sys.exit(0)
