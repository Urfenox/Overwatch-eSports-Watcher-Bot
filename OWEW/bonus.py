import time
import pyautogui # pip install pyautogui

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
        # busca un match en la area indicada
        bonus = pyautogui.locateOnScreen(image=str("{}\\bonus.png".format(self.WORKSPACE)), grayscale=True, region=self.MONITOR_AREA, confidence=0.8)
        if bonus != None:
            current_position = pyautogui.position()
            self.claimCount += 1
            self.lastClaim = time.strftime("%H:%M:%S", time.localtime())
            pyautogui.moveTo(bonus[0]+20, bonus[1]+15) # mueve al premio
            time.sleep(.5)
            pyautogui.click(button='left') # hace el click
            time.sleep(.5)
            pyautogui.moveTo(current_position) # restablece la posicion del cursor
            return True
        return False

    def printInformation(self):
        print("Monitor area: {}".format(self.MONITOR_AREA))
        print("[{}] claimed | Last claim [{}]".format(self.claimCount, self.lastClaim))
