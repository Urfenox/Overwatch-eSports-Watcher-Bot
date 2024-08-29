import os, time
import pyautogui # pip install pyautogui


# AQUI DEBES INDICAR LOS PASOS PARA EL SETUP DE TU NAVEGADOR WEB.
# A CONTINUACION SE MUESTRA UN EJEMPLO...

def setup(INSTANCE_INFO):
    time.sleep(1)

    os.spawnl(
        os.P_DETACH,
        INSTANCE_INFO["configuration"]["webbrowser"]["binary"],
        INSTANCE_INFO["configuration"]["webbrowser"]["arguments"]
    ) # inicia la instancia del navegador

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

    # time.sleep(5)

    # pyautogui.moveTo(1464, 830, duration=1) # selecciona la configuracion de transmision
    # pyautogui.click(button='left') # hace click

    # time.sleep(.5)

    # pyautogui.moveTo(1464, 630, duration=1) # selecciona calidad
    # pyautogui.click(button='left') # hace click

    # time.sleep(.5)

    # pyautogui.moveTo(1464, 660, duration=1) # selecciona 720p60
    # pyautogui.click(button='left') # hace click

    time.sleep(1)
    
    pyautogui.moveTo(1470, 960) # posiciona el cursor


# AQUI DEBES INDICAR LOS PASOS PARA EL BANISH DE LA ACCION FINALIZAR.
# A CONTINUACION SE MUESTRA UN EJEMPLO...

def banish(INSTANCE_INFO):
    pyautogui.hotkey('ctrl', 'f4') # cierra la pestaña activa

    time.sleep(0.2)

    pyautogui.hotkey('alt', 'f4') # cierra la ventana

    time.sleep(0.2)

    if INSTANCE_INFO["configuration"]["MUST_SHUTDOWN"]: # apaga el equipo
        os.system(str("shutdown.exe /s /t {}".format(INSTANCE_INFO["configuration"]["SHUTDOWN_TIME"]))) # apaga el equipo
    else: # suspende el equipo
        pyautogui.moveTo(20, 1060) # selecciona el icono Windows
        pyautogui.click(button='left') # hace clic

        time.sleep(0.5)

        pyautogui.moveTo(25, 1015) # selecciona el icono de Inicio/Apagado
        pyautogui.click(button='left') # hace clic

        time.sleep(0.5)

        pyautogui.moveTo(25, 900, duration=1) # selecciona el icono de Suspender
        pyautogui.click(button='left') # hace clic
