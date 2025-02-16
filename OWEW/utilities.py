import pathlib, time
import requests # pip install requests
import win32gui # pip install pywin32
import win32con # pip install pywin32
from PIL import ImageGrab, ImageDraw # pip install Pillow

class Utilities:
    # Propiedades
    WORKSPACE = None
    INSTANCE_INFO = None
    PUSHOVER_TOKEN = None
    PUSHOVER_USER = None
    PUSHOVER_DEVICE = None

    # Constructor
    def __init__(self, workspace: str, instance_info: dict):
        self.WORKSPACE = workspace
        self.INSTANCE_INFO = instance_info
        self.PUSHOVER_TOKEN = instance_info["configuration"]["PUSHOVER"]["TOKEN"]
        self.PUSHOVER_USER = instance_info["configuration"]["PUSHOVER"]["USER"]
        self.PUSHOVER_DEVICE = instance_info["configuration"]["PUSHOVER"]["DEVICE"]
        with open(str("{}\\logs.log".format(self.WORKSPACE)), "a") as logs:
            logs.write(str("\n\n\n"))

    # Variables

    # Metodos
    def AddToLog(self, content)->str: # mantiene un registro de lo que pasa
        try:
            log = str("{} {}".format(time.strftime("%H:%M:%S %d/%m", time.localtime()), content))
            print(log)
            with open(str("{}\\logs.log".format(self.WORKSPACE)), "a") as logs:
                logs.write(str(f"{log}\n"))
            return log
        except Exception as ex:
            pass
        return "Error"
        
    def SendScreenshot(self, mensaje, prioridad=1, ttl=60):
        try:
            imagePath = str("{}\\imagen.png".format(self.WORKSPACE))
            pathlib.Path.unlink(imagePath, missing_ok=True)
            screenshow = ImageGrab.grab(all_screens=True) # Take the screenshot
            draw = ImageDraw.Draw(screenshow)
            draw.rectangle(self.INSTANCE_INFO["configuration"]["MONITOR"]["AREA"][self.INSTANCE_INFO["configuration"]["MONITOR"]["SCREEN"]]["BONUS"])
            draw.rectangle(self.INSTANCE_INFO["configuration"]["MONITOR"]["AREA"][self.INSTANCE_INFO["configuration"]["MONITOR"]["SCREEN"]]["GAMBLES"])
            draw.rectangle(self.INSTANCE_INFO["configuration"]["MONITOR"]["AREA"][self.INSTANCE_INFO["configuration"]["MONITOR"]["SCREEN"]]["FINISHER"])
            screenshow.save(imagePath, "png")
            self.PushoverNotify(mensaje=str(mensaje), prioridad=prioridad, file=imagePath, ttl=ttl)
        except Exception as ex:
            self.AddToLog(str("[SendScreenshot]Error: {}".format(ex)))

    def PushoverNotify(self, mensaje, titulo = "OW eSports Watcher", prioridad = 0, file=None, ttl=0):
        try:
            if self.PUSHOVER_USER!="" and self.PUSHOVER_TOKEN!="":
                payload = {
                    "token": self.PUSHOVER_TOKEN,
                    "user": self.PUSHOVER_USER,
                    "device": self.PUSHOVER_DEVICE,
                    "title": titulo,
                    "message": mensaje,
                    "priority": prioridad
                }
                if ttl>0:
                    payload["ttl"] = ttl
                if file != None:
                    file = {"attachment": ("image.png", open(file, "rb"), "image/png")}
                r = requests.post("https://api.pushover.net/1/messages.json", data=payload, files=file)
                return self.AddToLog(str("({}) {}\n{}\n     ({})".format(prioridad, titulo, mensaje, r.text)))
            else:
                return self.AddToLog(str("({}) {}\n{}\n     (X)".format(prioridad, titulo, mensaje)))
        except Exception as ex:
            self.AddToLog(str("[PushoverNotify]Error: {}".format(ex)))
    
    def setTopMost(self, hwnd):
        try:
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 665, 0, 525, 170, 0)
        except Exception as ex:
            self.AddToLog(str("[setTopMost]Error: {}".format(ex)))
