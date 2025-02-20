import os, json, argparse

os.chdir(os.path.dirname(os.path.abspath(__file__)))

WORKSPACE = str(os.path.dirname(os.path.realpath(__file__)))
CONFIGURATION = json.load(open(str("{}\\config.json".format(WORKSPACE))))

def argumentos():
    parser = argparse.ArgumentParser(description='Overwatch eSports Watcher')
    parser.add_argument('-w', '--watch', type=str, help='Indica el canal a ver')
    parser.add_argument('-s', '--screen', type=str, help='Indica el monitor a monitorear')
    parser.add_argument('-c', '--check', type=str, help='Indica el tiempo para verificar')
    parser.add_argument('-a', '--awake', action='store_true', help='Omite el apagado del equipo al finalizar')
    parser.add_argument('-n', '--next', action='store_true', help='Omite el setup')
    args = parser.parse_args()
    if args.watch:
        CONFIGURATION["configuration"]["CHANNEL_NAME"] = str("twitch.tv/{}".format(str(args.watch).strip()))
    if args.screen:
        CONFIGURATION["configuration"]["MONITOR"]["SCREEN"] = int(str(args.screen).strip())
    if args.check:
        CONFIGURATION["configuration"]["WAIT_TIME"] = int(str(args.check).strip())
    if args.awake:
        CONFIGURATION["configuration"]["SHUTDOWN_TIME"] = False
    if args.next:
        CONFIGURATION["configuration"]["CHANNEL_NAME"] = False


# TESTING ONLY
if __name__ == "__main__":
    import os, json, winsound
    print("Este archivo se ejecutó directamente")
    argumentos()
    winsound.Beep(2500, 500)
    winsound.Beep(2500, 500)
    os.system("pause")
