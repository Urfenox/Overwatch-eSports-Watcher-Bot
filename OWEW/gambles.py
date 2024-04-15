import pyautogui # pip install pyautogui

class GambleCatcher:
    # Propiedades
    MONITOR_AREA = []
    WORKSPACE = None

    # Constructor
    def __init__(self, monitor_area, workspace):
        self.MONITOR_AREA = monitor_area
        self.WORKSPACE = workspace

    # Variables

    # Metodos
    def checkForGamble(self)->bool:
        try:
            # busca un match en la area indicada
            gamble = pyautogui.locateOnScreen(str("{}\\gamble.png".format(self.WORKSPACE)), grayscale=True, region=self.MONITOR_AREA, confidence=0.8)
            if gamble != None:
                return True
        except:
            return False
        return False
