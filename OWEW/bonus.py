import time
import pyautogui # pip install pyautogui
from PIL import ImageChops # pip install pillow
from PIL import ImageGrab # pip install pillow

class BonusCatcher:
    # Propiedades
    MONITOR_AREA = []
    MOUSE_MOVES = []

    # Constructor
    def __init__(self, monitor_area, mouse_moves = [(1690, 940), (1690, 980)]):
        self.MONITOR_AREA = monitor_area
        self.MOUSE_MOVES = mouse_moves

    # Variables
    claimCount = 0
    lastClaim = "NA"
    imgBase = None

    # Metodos
    def createBase(self):
        # crea una base para obtener diferencias posteriormente
        self.imgBase = ImageGrab.grab(bbox=self.MONITOR_AREA, all_screens=True)

    def checkBase(self)->bool:
        # verifica que la situacion actual sea igual a la base original
        diff = ImageChops.difference(ImageGrab.grab(bbox=self.MONITOR_AREA, all_screens=True), self.imgBase)
        bbox = diff.getbbox()
        if bbox is not None:
            current_position = pyautogui.position()
            self.claimCount += 1
            self.lastClaim = time.strftime("%H:%M:%S", time.localtime())
            pyautogui.moveTo(self.MOUSE_MOVES[0][0], self.MOUSE_MOVES[0][1], duration=.5) # evita el tooltip del contador
            pyautogui.moveTo(self.MOUSE_MOVES[1][0], self.MOUSE_MOVES[1][1], duration=.5) # mueve al premio
            time.sleep(.5)
            pyautogui.click(button='left') # hace el click
            time.sleep(.5)
            pyautogui.moveTo(current_position) # restablece la posicion del cursor
            return True
        return False

    def printInformation(self):
        print("Monitor area: {}".format(self.MONITOR_AREA))
        print("[{}] claimed | Last claim [{}]\n".format(self.claimCount, self.lastClaim))
