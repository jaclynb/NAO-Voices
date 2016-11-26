# -*- encoding: UTF-8 -*-

"""
Usage:
  voices.py VOICE STORY ROBOTIP 
  voices.py (-h | --help)
Examples:
  voices.py cartoon BoyWhoCriedWolf 141.219.141.219 
  voices.py robot Goldilocks 141.219.141.219 
  voices.py natural ThreePigs 141.219.141.219
Options:
  -h, --help
"""

from naoqi import ALProxy
from docopt import docopt

def main(arguments):
    voice = arguments.pop("VOICE", None)
    if (voice == None):
        sys.exit("Missing voice argument")

    story = arguments.pop("STORY", None)
    if (story == None):
        sys.exit("Missing story argument")

    robotIP = arguments.pop("ROBOTIP", None)
    if (robotIP == None):
        robotIP = "127.0.0.1"

    port = 9559


    audio = ALProxy("ALAudioPlayer", robotIP, port)

    #Need to have files on Nao to play
    #fileName = "/usr/share/naoqi/wav/random.wav"
    fileName = "audio/" + voice + "/" + story + ".wav"

    fileID = audio.playFile(fileName)


if __name__ == "__main__":
    arguments = docopt(__doc__)

    main(arguments)