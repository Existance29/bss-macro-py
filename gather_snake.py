import pyautogui as pag
import os
import tkinter
import move
import loadsettings
setdat = loadsettings.load()
sizeword = setdat["gather_size"]
width = setdat["gather_width"]/2
size = 0
if sizeword.lower() == "s":
    size = 1
elif sizeword.lower() == "m":
    size =1.5
else:
    size = 2

for i in range(2):
    move.hold("w", 0.72*size)
    move.hold("a", 0.1*width)
    move.hold("s", 0.72*size)
    move.hold("a", 0.1*width)
for i in range(2):
    move.hold("w", 0.72*size)
    move.hold("d", 0.1*width)
    move.hold("s", 0.72*size)
    move.hold("d", 0.1*width)
        
    
    