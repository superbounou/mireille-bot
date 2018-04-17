"""This class manage the CLI interaction"""
import json
import logging
import sys
import ConfigParser
from .audio import Audio
from .speech import Speech
from .bot import Bot

LOGGER = logging.getLogger(__name__)
CONFIG = ConfigParser.ConfigParser()

#pylint: disable=invalid-name
class AudioStage(object): # pylint: disable=too-few-public-methods
    """This class manage CLI interactions"""
    @staticmethod
    def record(): # pylint: disable=invalid-name
        """FOO"""
        audio = Audio()
        audio.record_to_file('test.wav')

    @staticmethod
    def read(): # pylint: disable=invalid-name
        """Read input sound"""
        speech = Speech()
        print speech.get_words('test.wav')

#pylint: disable=invalid-name
class BotStage(object): # pylint: disable=too-few-public-methods
    @staticmethod
    def conversation(): # pylint: disable=invalid-name
        """Read input sound"""
        bot = Bot()
        bot.conversation()


class Cli(object):# pylint: disable=too-few-public-methods
    """CLI class"""
    def __init__(self):
        """CLI constructor"""
        self.audio = AudioStage()
        self.bot = BotStage()
