import pywhatkit
import random
import time
import pyautogui

wishes = [ "Hello 😄","How are you?","Python automation!","This is auto message","Good day!"]
number = "+91xxxxxxxxxx"

len_of_msgs = 5
gap_of_msgs = 5

for i in range(len_of_msgs):
    msg = random.choice(wishes)
    pywhatkit.sendwhatmsg_instantly(number,msg,True)
    time.sleep(gap_of_msgs)
    pyautogui.press('enter')
    time.sleep(gap_of_msgs)




