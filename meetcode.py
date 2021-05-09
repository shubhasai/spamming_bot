import pyautogui
# import webbrowser as wb
import time
time.sleep(15)
msg = "No sound and screen not visible"
# pyautogui.moveTo(1070, 100)
pyautogui.click()
for i in range(50):
    # pyautogui.moveTo(1070, 100)
    # pyautogui.click()
    pyautogui.typewrite(msg)
    pyautogui.press("enter")