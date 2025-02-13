import os, json, argparse

os.chdir(os.path.dirname(os.path.abspath(__file__)))

WORKSPACE = str(os.path.dirname(os.path.realpath(__file__)))
CONFIGURATION = json.load(open(str("{}\\config.json".format(WORKSPACE))))

def argumentos():
    parser = argparse.ArgumentParser(description='Overwatch eSports Watcher')
    parser.add_argument('-w', '--watch', type=str, help='Indica el canal a ver')
    parser.add_argument('-s', '--screen', type=str, help='Indica el monitor a monitorear')
    args = parser.parse_args()
    if args.watch:
        CONFIGURATION["configuration"]["CHANNEL_NAME"] = str("twitch.tv/{}".format(str(args.watch).strip()))
    if args.screen:
        CONFIGURATION["configuration"]["MONITOR"]["SCREEN"] = int(str(args.screen).strip())
