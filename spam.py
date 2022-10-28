import pyautogui as gui 
import time 
import random, string

num = int(input())
massage = input()
time.sleep(10)
#palavra = input()
for i in range(num):
    gui.typewrite(massage)
    gui.press("Enter")

