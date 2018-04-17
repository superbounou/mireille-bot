"""Class example"""
import time
import ConfigParser

CONFIG = ConfigParser.ConfigParser()
CONFIG.read("mireille.cfg")

from .audio import Audio
from .cloud import Cloud

class Bot(object):

    def conversation(self):
        while True:
            audio = Audio()
            audio.record_to_file('test.wav')
            cloud = Cloud()
            print cloud.get_words('test.wav')
            print("continue ...")
            time.sleep(3)
