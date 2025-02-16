import os, time, ctypes
import pyautogui # pip install pyautogui
import win32api
import win32security

# AQUI DEBES INDICAR LOS PASOS PARA EL SETUP DE TU NAVEGADOR WEB.
# A CONTINUACION SE MUESTRA UN EJEMPLO...

def setup(INSTANCE_INFO):
    time.sleep(1)

    os.spawnl(
        os.P_DETACH,
        INSTANCE_INFO["configuration"]["webbrowser"]["binary"], # ejecutable
        INSTANCE_INFO["configuration"]["webbrowser"]["arguments"] # argumentos
    ) # inicia la instancia del navegador

    time.sleep(5) # da tiempo a abrir el navegador

    pyautogui.moveTo(100, 1) # pone el cursor en la pestaña principal
    pyautogui.click(button='left') # hace clic en la pestaña para hacer focus en el navegador

    time.sleep(1)

    for i in range(5):
        pyautogui.hotkey('ctrl', 'f4') # cierra la pestaña
        time.sleep(.5)

    pyautogui.hotkey('ctrl', '1') # selecciona la primera pestaña

    time.sleep(1)

    pyautogui.hotkey('ctrl', 'l') # selecciona la barra de direcciones

    time.sleep(1)

    pyautogui.typewrite(INSTANCE_INFO["configuration"]["CHANNEL_NAME"], interval=0.2) # escribe twitch.tv/...
    pyautogui.press('enter') # presiona enter para buscar el canal

    # time.sleep(10) # da tiempo el sitio
    # pyautogui.moveTo(1000, 350, duration=2) # seleccionar el banner del canal
    # pyautogui.click(button='left') # hace clic en el banner para ver la transmision

    time.sleep(10) # da tiempo para cargar la transmision

    pyautogui.moveTo(1545, 950, duration=1) # posiciona el cursor


# AQUI DEBES INDICAR LOS PASOS PARA EL FIN DE LOS TIEMPOS.
# A CONTINUACION SE MUESTRA UN EJEMPLO...

def conclude(hibernate=False):
    priv_flags = (win32security.TOKEN_ADJUST_PRIVILEGES |
                  win32security.TOKEN_QUERY)
    hToken = win32security.OpenProcessToken(
        win32api.GetCurrentProcess(),
        priv_flags
    )
    priv_id = win32security.LookupPrivilegeValue(
       None,
       win32security.SE_SHUTDOWN_NAME
    )
    old_privs = win32security.AdjustTokenPrivileges(
        hToken,
        0,
        [(priv_id, win32security.SE_PRIVILEGE_ENABLED)]
    )

    if (win32api.GetPwrCapabilities()['HiberFilePresent'] == False and
        hibernate == True):
            import warnings
            warnings.warn("Hibernate isn't available. Suspending.")
    try:
        ctypes.windll.powrprof.SetSuspendState(not hibernate, True, False)
    except:
        win32api.SetSystemPowerState(not hibernate, True)

    # Restore previous privileges
    win32security.AdjustTokenPrivileges(
        hToken,
        0,
        old_privs
    )


# TESTING ONLY
if __name__ == "__main__":
    import os, json, winsound
    print("Este archivo se ejecutó directamente")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    WORKSPACE = str(os.path.dirname(os.path.realpath(__file__)))
    CONFIGURATION = json.load(open(str("{}\\config.json".format(WORKSPACE))))
    setup(CONFIGURATION)
    winsound.Beep(2500, 500)
    winsound.Beep(2500, 500)
    os.system("pause")
