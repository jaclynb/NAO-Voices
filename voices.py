# -*- encoding: UTF-8 -*-

"""
Usage:
  voices.py VOICE STORY ROBOTIP 
  voices.py (-h | --help)
Examples:
  voices.py cartoon boywhocriedwolf 141.219.141.219 
  voices.py robot goldilocks 141.219.141.219 
  voices.py natural threepigs 141.219.141.219
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
    for i in range(7):
      fileName = "/var/persistent/home/nao/voicesaudio/" + voice + "/" + story + str(i+1) + ".wav"
      fileID = audio.playFile(fileName)
      pause = raw_input("Press enter to continue")

if __name__ == "__main__":
    arguments = docopt(__doc__)

    main(arguments)