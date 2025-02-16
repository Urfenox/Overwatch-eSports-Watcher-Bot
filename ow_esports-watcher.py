from OWEW.utilities import Utilities
from OWEW.config import *
from datetime import datetime
import time, os, sys
import win32gui # pip install pywin32
os.system("cls")

os.chdir(os.path.dirname(os.path.abspath(__file__)))

argumentos()

WORKSPACE = str("{}\\OWEW".format(os.path.dirname(os.path.realpath(__file__))))
CONFIGURATION["started"] = datetime.now()
MONITOR = CONFIGURATION["configuration"]["MONITOR"]["SCREEN"]
os.system(str("title {}".format(CONFIGURATION["title"])))

util = Utilities(
    WORKSPACE,
    CONFIGURATION
)

time.sleep(1) # hace que setTopMost funcione, idk why lol
util.setTopMost(win32gui.FindWindow(None, CONFIGURATION["title"]))

print("Workspace {}".format(WORKSPACE))

from OWEW.steps import setup, conclude
try:
    util.AddToLog("Dirigiéndose a la transmisión...")
    print("    CTRL+C para omitir.")
    os.system(str("timeout 5"))
    util.PushoverNotify(mensaje=str("¡Iniciando {}!".format(CONFIGURATION["title"])), prioridad=1)
    setup(CONFIGURATION)
    os.system("cls")
except KeyboardInterrupt:
    os.system("cls")
    util.AddToLog("Setup skipped...")

from OWEW.bonus import BonusCatcher
from OWEW.gambles import GambleCatcher
from OWEW.finisher import FinisherCatcher

print("Creando instancias...")
time.sleep(1)
print("    Bonus area: {}".format(CONFIGURATION["configuration"]["MONITOR"]["AREA"][MONITOR]["BONUS"]))
print("    Finish area: {}".format(CONFIGURATION["configuration"]["MONITOR"]["AREA"][MONITOR]["FINISHER"]))
bc = BonusCatcher(CONFIGURATION["configuration"]["MONITOR"]["AREA"][MONITOR]["BONUS"], WORKSPACE)
gc = GambleCatcher(CONFIGURATION["configuration"]["MONITOR"]["AREA"][MONITOR]["GAMBLES"], WORKSPACE)
fc = FinisherCatcher(CONFIGURATION["configuration"]["MONITOR"]["AREA"][MONITOR]["FINISHER"])
fc.createBase() # crea una imagen de referencia
time.sleep(1)
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
        uptime = fc.getUptime(CONFIGURATION["started"])
        CONFIGURATION["uptime"] = str("{}h:{}m:{}s".format(uptime[0], uptime[1], uptime[2]))
        util.PushoverNotify(mensaje=str("¡Transmisión finalizada!\nUptime: {}\nClaimed: {}\nPredictions: {}".format(
            CONFIGURATION["uptime"],
            bc.claimCount,
            gc.predictCount)))
        os.system(str("timeout {}".format(CONFIGURATION["configuration"]["SHUTDOWN_TIME"]))); conclude() # suspende el equipo
        # os.system(str("shutdown.exe /s /t {}".format(CONFIGURATION["configuration"]["SHUTDOWN_TIME"]))) # apaga el equipo
        sys.exit(0)
    os.system(str("timeout {}".format(CONFIGURATION["configuration"]["WAIT_TIME"])))
