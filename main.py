import pyautogui
import webbrowser as wb
import time
def emoji():
    pyautogui.moveTo(440, 685)
    pyautogui.click() 
    pyautogui.moveTo(445, 495)
    pyautogui.click() 
    pyautogui.click()
    pyautogui.press("enter")

word = "U r hacked af"
msg = "Bot By Shubhasai Activated"
clngmsg = "Task Completed sir"
wb.open("https://web.whatsapp.com/")
time.sleep(50)
pyautogui.typewrite(msg)
pyautogui.press("enter")
for i in range(120):
    pyautogui.typewrite(word)
    time.sleep(1)
    pyautogui.press("enter")
    #emoji()

# emoji()
# pyautogui.press("enter")
pyautogui.typewrite(clngmsg)
pyautogui.press("enter")