from PIL import ImageGrab,ImageOps
import time
import pyautogui
from numpy import *
import sys
sys.setrecursionlimit(2500)

class Cordinates():
    replayBtn = (482,460)
    dinosaur = (187,460)

def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    print("Jump")
    pyautogui.keyUp('space')

def imageGrab():
    box = (Cordinates.dinosaur[0]+53,Cordinates.dinosaur[1]+10,Cordinates.dinosaur[0]+135,Cordinates.dinosaur[1]+45)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return(a.sum())

def main():
    restartGame()
    while True:
        if (imageGrab() !=3117):
            pressSpace()
        main()

main()





