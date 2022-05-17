#imports needed
import time
import pyautogui
import datetime




minutes = 1
    
while minutes<60:
	now = datetime.datetime.today()
	pyautogui.screenshot('/home/kali/Documents/Keylogger/Screenshots/'+str(now)+'.png')
	minutes+=1
	time.sleep(60)
