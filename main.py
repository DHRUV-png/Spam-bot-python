#importing libarys
import pyautogui
import time

time.sleep(5)


spam_text = "this is spam"
for _ in range(20):
    pyautogui.typewrite(spam_text)
    pyautogui.press("enter")
    time.sleep(1)
