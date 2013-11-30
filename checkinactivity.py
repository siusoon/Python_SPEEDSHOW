# logic: detect idle time from mac os (mouse and keyboard) and force to go to a specific website
# to run the program, administrator needs to set the sleeptime, temp_idle_value and url
# Firefox should be the default browser, hide all other applications and docking on the screen
# set no screensaver

# install fullscreen firefox add-ons (to maintain the full screen mode of your firefox browser): https://addons.mozilla.org/en-US/firefox/addon/resizeit/contribute/roadblock/?src=search&version=3.6.2
# put the file in desktop, then open terminal to go to Desktop directory, type: python [filename] 

import sys,os,time
import webbrowser

# define variable
sleeptime = 10  #how frequent to get the idle time
temp_idle_value = 60  #Duration to reset browser (in sec format)
url = "http://www.facebook.com"

def main_loop():
    while 1:

		time.sleep(sleeptime)
		cmd = "ioreg -c IOHIDSystem | perl -ane 'if (/Idle/) {$idle=(pop @F)/1000000000; print $idle}'"
		result = os.popen(cmd)  #use popen instead of os.system to open a perl script
		str = result.read()
		temp_idle = int(str.split(".")[0])
		#print(str)
		
  		if temp_idle > temp_idle_value and status == 0:
  			resetBrowser()
  			status = 1
  			
  		elif temp_idle > temp_idle_value and status == 1:
  			print("do nothing")
  			
  		else:
  			print("continue")
  			status = 0

def resetBrowser():
	result1 = os.system("ps axo pid,command | grep '[f]irefox'")  #256 means not active, else will display a whole line
	if result1 == 256:
		print("firefox is inactive -> start a browser")
		webbrowser.open_new(url)   #workable
	else:
		print("should kill the browser then open a firefox")
		os.system("killall -9 firefox")
		time.sleep(5)  
		webbrowser.get("firefox")
		webbrowser.open(url, new=0, autoraise=False)
		

if __name__ == '__main__':
    
    try:
        status = 0
        main_loop()
    except KeyboardInterrupt:  #control+c in mac
   		print ('stop')
    sys.exit(0)


	
