import pyautogui
import csv
import time

def Test():
    a = open('Cracked Earth - Gate2Flag.csv')
    b = csv.reader(a)
    c = list(b)
    pyautogui.moveTo(int(c[0][0]),int(c[0][1]))
    for i in c:
        pyautogui.mouseDown()
        pyautogui.moveTo(int(i[0]),int(i[1]))
        pyautogui.mouseDown()
        time.sleep(float(i[2]))
    pyautogui.mouseUp()

Test()
