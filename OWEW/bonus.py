import time
import cv2 as cv # pip install opencv-python
import pyautogui # pip install pyautogui
from PIL import ImageGrab # pip install Pillow
import numpy as np # pip install numpy

class BonusCatcher:
    # Propiedades
    MONITOR_AREA = []
    WORKSPACE = None

    # Constructor
    def __init__(self, monitor_area, workspace):
        self.MONITOR_AREA = monitor_area
        self.WORKSPACE = workspace

    # Variables
    claimCount = 0
    lastClaim = "NA"

    # Metodos
    def checkForBonus(self)->bool:
        try:
            # busca un match en la area indicada
            pajar = np.array(ImageGrab.grab(all_screens=True).convert('RGB')) # A L L  S C R E E N S
            aguja = cv.imread(str("{}\\bonus.png".format(self.WORKSPACE)), cv.IMREAD_UNCHANGED)
            bonus = cv.matchTemplate(pajar, aguja, cv.TM_CCOEFF_NORMED) # DAMN, OpenCV moment
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(bonus)
            if max_val >= 0.75:
                current_position = pyautogui.position()
                self.claimCount += 1
                self.lastClaim = time.strftime("%H:%M:%S", time.localtime())
                pyautogui.moveTo(max_loc[0]+20, max_loc[1]+15) # mueve al premio
                time.sleep(.5)
                pyautogui.click(button='left') # hace el click
                time.sleep(.5)
                pyautogui.moveTo(current_position) # restablece la posicion del cursor
                return True
        except:
            return False
        return False

    def printInformation(self):
        print("[{}] claimed | Last claim [{}]".format(self.claimCount, self.lastClaim))
