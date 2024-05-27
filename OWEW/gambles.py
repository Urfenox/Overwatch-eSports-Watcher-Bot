import time
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
    newGamble = True
    predictCount = 0
    lastPredict = "NA"

    # Metodos
    def checkForGamble(self)->bool:
        try:
            # busca un match en la area indicada
            gamble = pyautogui.locateOnScreen(str("{}\\gamble.png".format(self.WORKSPACE)), grayscale=True, region=self.MONITOR_AREA, confidence=0.8)
            if gamble != None: # si hay una prediccion
                # verifica que sea nueva (para evitar notificar una prediccion varias veces mientras esta activa)
                if self.newGamble: # si es nueva
                    self.predictCount += 1
                    self.lastPredict = time.strftime("%H:%M:%S", time.localtime())
                    self.newGamble = False # indica que la prediccion actual ya esta notificada
                    return True # devuelve True, hay una prediccion nueva!
            else: # si no hay una prediccion
                self.newGamble = True # indica que no hay predicciones nuevas
        except: # en nuevas versiones de PyAutoGUI, si no se encuentra se genera un error
            return False
        return False # sin predicciones (defecto)
    
    def printInformation(self):
        print("[{}] predictions | Last prediction [{}]".format(self.predictCount, self.lastPredict))
