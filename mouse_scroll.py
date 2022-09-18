from xml.dom.minidom import parseString
import pyautogui
import time
for i in range(20):
    try:
        time.sleep(1)
        pyautogui.scroll(i*10)
    except:
        pass