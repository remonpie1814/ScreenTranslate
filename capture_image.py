import pyautogui
import cv2
import numpy as np
import os

def capture_area(area):
    if "savedScreen.png" in os.listdir():
        a = pyautogui.screenshot(region=area)
        img = np.array(a)
        img2 = cv2.imread('savedScreen.png')
        location = pyautogui.locateOnScreen('savedScreen.png')
        if location != None:
            return False
        else:
            a.save('savedScreen.png')
            return True
    else:
        a = pyautogui.screenshot(region=area)
        img = np.array(a)
        a.save('savedScreen.png')
        return True
if __name__ == '__main__':
    a = pyautogui.screenshot(region=(0,0,20,20))
    img = np.array(a)
    a.save('test.png')
    location1 = pyautogui.locateOnScreen('test.png')
    print(location1)
    print(location1.left,location1.top,location1.width,location1.height)