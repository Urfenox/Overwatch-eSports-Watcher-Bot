from OWEW.utilities import Utilities
from datetime import datetime
import time, os, sys, json
import pyautogui # pip install pyautogui
import win32gui # pip install pywin32
os.system("cls")

os.chdir(os.path.dirname(os.path.abspath(__file__)))

WORKSPACE = str("{}\\OWEW".format(os.path.dirname(os.path.realpath(__file__))))
INSTANCE_INFO = json.load(open(str("{}\\config.json".format(WORKSPACE))))
INSTANCE_INFO["started"] = datetime.now()
MONITOR = INSTANCE_INFO["configuration"]["MONITOR"]["SCREEN"]
os.system(str("title {}".format(INSTANCE_INFO["title"])))

util = Utilities(
    WORKSPACE,
    INSTANCE_INFO["configuration"]["PUSHOVER"]["TOKEN"],
    INSTANCE_INFO["configuration"]["PUSHOVER"]["USER"],
    INSTANCE_INFO["configuration"]["PUSHOVER"]["DEVICE"])

time.sleep(1) # hace que setTopMost funcione, idk why lol
util.setTopMost(win32gui.FindWindow(None, INSTANCE_INFO["title"]))

print("Workspace {}".format(WORKSPACE))

# Inicia el Setup
try:
    util.AddToLog("Dirigiéndose a la transmisión...")
    print("    CTRL+C para omitir.")
    os.system(str("timeout 5"))
    util.PushoverNotify(mensaje=str("¡Iniciando {}!".format(INSTANCE_INFO["title"])), prioridad=1)
    time.sleep(1)
    os.spawnl(os.P_DETACH, INSTANCE_INFO["configuration"]["webbrowser"]["binary"], INSTANCE_INFO["configuration"]["webbrowser"]["arguments"]) # inicia la instancia del navegador
    time.sleep(5)
    pyautogui.moveTo(100, 1) # selecciona la barra del navegador
    pyautogui.click(button='left') # hace clic en la pestaña para hacer focus en el navegador
    time.sleep(.5)
    pyautogui.hotkey('ctrl', 'l') # selecciona la barra de direcciones
    time.sleep(1)
    pyautogui.typewrite(INSTANCE_INFO["configuration"]["CHANNEL_NAME"], interval=0.2) # escribe twitch.tv/ow_esports
    pyautogui.press('enter') # presiona enter para buscar el canal
    time.sleep(5)
    pyautogui.moveTo(1000, 350, duration=2) # seleccionar el banner del canal
    pyautogui.click(button='left') # hace clic en el banner para ver la transmision
    time.sleep(5)
    pyautogui.moveTo(1464, 823, duration=1) # selecciona la configuracion de transmision
    pyautogui.click(button='left') # hace click
    time.sleep(.5)
    pyautogui.moveTo(1464, 580, duration=1) # selecciona calidad
    pyautogui.click(button='left') # hace click
    time.sleep(.5)
    pyautogui.moveTo(1280, 720, duration=1) # selecciona 480p
    pyautogui.click(button='left') # hace click
    time.sleep(1)
    pyautogui.moveTo(1160, 860, duration=1) # posiciona el cursor
except KeyboardInterrupt:
    util.AddToLog("Setup skipped...")

from OWEW.bonus import BonusCatcher
from OWEW.gambles import GambleCatcher
from OWEW.finisher import FinisherCatcher

print("Creando instancias...")
time.sleep(5)
print("    Bonus area: {}".format(INSTANCE_INFO["configuration"]["MONITOR"]["AREA"][MONITOR]["BONUS"]))
print("    Finish area: {}".format(INSTANCE_INFO["configuration"]["MONITOR"]["AREA"][MONITOR]["FINISHER"]))
bc = BonusCatcher(INSTANCE_INFO["configuration"]["MONITOR"]["AREA"][MONITOR]["BONUS"], WORKSPACE)
gc = GambleCatcher(INSTANCE_INFO["configuration"]["MONITOR"]["AREA"][MONITOR]["GAMBLES"], WORKSPACE)
fc = FinisherCatcher(INSTANCE_INFO["configuration"]["MONITOR"]["AREA"][MONITOR]["FINISHER"])
fc.createBase() # crea una imagen de referencia
time.sleep(5)
util.SendScreenshot("Estado de la instancia", ttl=120)

while True:
    os.system("cls")
    bc.printInformation()
    gc.printInformation()
    util.AddToLog("Buscando diferencias...")
    if bc.checkForBonus():
        util.AddToLog("Bonificación encontrada!")
    if gc.checkForGamble():
        util.PushoverNotify(mensaje="Predicción iniciada!", ttl=60)
    if fc.checkBase():
        util.AddToLog("La transmisión ha finalizado!")
        uptime = fc.getUptime(INSTANCE_INFO["started"])
        INSTANCE_INFO["uptime"] = str("{}h:{}m:{}s".format(uptime[0], uptime[1], uptime[2]))
        util.PushoverNotify(mensaje=str("¡Transmisión finalizada!\nUptime: {}\nClaimed: {}".format(
            INSTANCE_INFO["uptime"],
            bc.claimCount)))
        os.system(str("shutdown.exe /s /t {}".format(INSTANCE_INFO["configuration"]["SHUTDOWN_TIME"]))) # apaga el equipo
        sys.exit(0)
    os.system(str("timeout {}".format(INSTANCE_INFO["configuration"]["WAIT_TIME"])))
