import time
import cv2 as cv # pip install opencv-python
from PIL import ImageGrab # pip install Pillow
import numpy as np # pip install numpy

class GambleCatcher:
    # Propiedades
    MONITOR_AREA = []
    WORKSPACE = None

    # Constructor
    def __init__(self, monitor_area, workspace):
        self.MONITOR_AREA = monitor_area
        self.WORKSPACE = workspace

    # Variables
    newGamble = True
    predictCount = 0
    lastPredict = "NA"

    # Metodos
    def checkForGamble(self)->bool:
        try:
            # busca un match en la area indicada
            pajar = np.array(ImageGrab.grab(all_screens=True).convert('RGB')) # A L L  S C R E E N S
            aguja = cv.imread(str("{}\\gamble.png".format(self.WORKSPACE)), cv.IMREAD_UNCHANGED)
            gamble = cv.matchTemplate(pajar, aguja, cv.TM_CCOEFF_NORMED) # DAMN, OpenCV moment
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(gamble)
            if max_val >= 0.75:
                if self.newGamble: # si es nueva
                    self.predictCount += 1
                    self.lastPredict = time.strftime("%H:%M:%S", time.localtime())
                    self.newGamble = False # indica que la prediccion actual ya esta notificada
                    return True # devuelve True, hay una prediccion nueva!
            else: # si no hay una prediccion
                    self.newGamble = True # indica que no hay predicciones nuevas
        except Exception as ex: # en nuevas versiones de PyAutoGUI, si no se encuentra se genera un error
            self.newGamble = True # si falla no encuentra, si no encuentra restablecemos
            self.AddToLog(str("[!]{}".format(ex)))
            return False
        return False # sin predicciones (defecto)
    
    def printInformation(self):
        print("[{}] predictions | Last prediction [{}]".format(self.predictCount, self.lastPredict))
    
    def AddToLog(self, content)->str: # mantiene un registro de lo que pasa
        log = str("GAMBLES {} {}".format(time.strftime("%H:%M:%S %d/%m", time.localtime()), content))
        with open(str("{}\\logs.log".format(self.WORKSPACE)), "a") as logs:
            logs.write(str(f"{log}\n"))
        return log
