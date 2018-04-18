"""Bot class"""
import ConfigParser

from chatterbot import ChatBot
from .audio import Audio
from .speech import Speech

CONFIG = ConfigParser.ConfigParser()
CONFIG.read("mireille.cfg")

class Bot(object):
    """Manage Bot interactions"""
    @staticmethod
    def conversation():
        """Start conversation with the bot"""
        silence = 0
        while True:
            audio = Audio()
            audio.record_to_file('test.wav')
            speech = Speech()
            sentence = speech.get_words('test.wav')
            print sentence
            silence = silence + 1 if sentence is None else silence
            if silence > 1:
                return 0

    @staticmethod
    def traine():
        """Traine the bot"""
        bot = ChatBot(
            'Charlie',
            trainer='chatterbot.trainers.ListTrainer'
        )
        bot.train()
