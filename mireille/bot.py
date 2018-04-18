"""Class example"""
import time
import ConfigParser

from chatterbot import ChatBot
from .audio import Audio
from .speech import Speech

CONFIG = ConfigParser.ConfigParser()
CONFIG.read("mireille.cfg")

class Bot(object):

    def conversation(self):
        silence = 0
        while True:
            audio = Audio()
            audio.record_to_file('test.wav')
            speech = Speech()
            sentence = speech.get_words('test.wav')
            print sentence
            silence = silence + 1 if sentence is None else silence
            if silence > 1:
                print("Ok bye !")
                break
                
    def traine(self):
        bot = ChatBot(
            'Charlie',
            trainer='chatterbot.trainers.ListTrainer'
        )
