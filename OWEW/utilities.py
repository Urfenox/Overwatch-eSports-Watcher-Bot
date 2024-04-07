import time
import requests # pip install requests
import win32gui # pip install pywin32
import win32con # pip install pywin32

class Utilities:
    # Propiedades
    WORKSPACE = None
    PUSHOVER_TOKEN = None
    PUSHOVER_USER = None
    PUSHOVER_DEVICE = None

    # Constructor
    def __init__(self, workspace: str, pushover_token: str, pushover_user: str, pushover_device: str):
        self.WORKSPACE = workspace
        self.PUSHOVER_TOKEN = pushover_token
        self.PUSHOVER_USER = pushover_user
        self.PUSHOVER_DEVICE = pushover_device
        with open(str("{}\\logs.log".format(self.WORKSPACE)), "a") as logs:
            logs.write(str("\n\n\n"))

    # Variables

    # Metodos
    def AddToLog(self, content)->str: # mantiene un registro de lo que pasa
        log = str("{} {}".format(time.strftime("%H:%M:%S %d/%m", time.localtime()), content))
        print(log)
        with open(str("{}\\logs.log".format(self.WORKSPACE)), "a") as logs:
            logs.write(str(f"{log}\n"))
        return log
    
    def PushoverNotify(self, mensaje, titulo = "OW eSports Watcher", prioridad = 0):
        if self.PUSHOVER_USER!=None and self.PUSHOVER_TOKEN!=None:
            r = requests.post("https://api.pushover.net/1/messages.json", data = {
                "token": self.PUSHOVER_TOKEN,
                "user": self.PUSHOVER_USER,
                "device": self.PUSHOVER_DEVICE,
                "title": titulo,
                "message": mensaje,
                "priority": prioridad
            })
            return self.AddToLog(str("({}) {}\n{}\n     ({})".format(prioridad, titulo, mensaje, r.text)))
        else:
            return self.AddToLog(str("({}) {}\n{}\n     (X)".format(prioridad, titulo, mensaje)))
    
    def setTopMost(self, hwnd):
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 665, 1, 525, 200, 0)
