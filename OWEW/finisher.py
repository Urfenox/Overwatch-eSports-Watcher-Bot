import time
from PIL import ImageChops # pip install pillow
from PIL import ImageGrab # pip install pillow
from datetime import datetime

class FinisherCatcher:
    # Propiedades
    MONITOR_AREA = []
    CLOSE_BUTTON = []

    # Constructor
    def __init__(self, monitor_area, close_button = (1910, 10)):
        self.MONITOR_AREA = monitor_area
        self.CLOSE_BUTTON = close_button

    # Variables
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
            return True # el streaming termino
        return False # el streaming sigue

    def getUptime(self, timestamp: datetime)->list:
        duration = datetime.now() - timestamp
        duration_in_s = duration.total_seconds()
        days = divmod(duration_in_s, 86400)
        hours = divmod(days[1], 3600)
        minutes = divmod(hours[1], 60)
        seconds = divmod(minutes[1], 1)
        return [round(hours[0]), round(minutes[0]), round(seconds[0])]
