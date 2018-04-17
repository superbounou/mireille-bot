"""This class manage the CLI interaction"""
import json
import logging
import sys
import ConfigParser
from .audio import Audio
from .cloud import Cloud

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
        cloud = Cloud()
        print cloud.get_words('test.wav')



class Cli(object):# pylint: disable=too-few-public-methods
    """CLI class"""
    def __init__(self):
        """CLI constructor"""
        self.audio = AudioStage()
