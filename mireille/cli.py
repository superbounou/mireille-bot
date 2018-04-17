"""This class manage the CLI interaction"""
import json
import logging
import sys
import ConfigParser

LOGGER = logging.getLogger(__name__)
CONFIG = ConfigParser.ConfigParser()

#pylint: disable=invalid-name
class ExampleStage(object): # pylint: disable=too-few-public-methods
    """This class manage CLI interactions"""
    @staticmethod
    def foo(): # pylint: disable=invalid-name
        """FOO"""
        print("foo")


class Cli(object):# pylint: disable=too-few-public-methods
    """CLI class"""
    def __init__(self):
        """CLI constructor"""
        self.stage = ExampleStage()
