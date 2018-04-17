"""Class example"""
import time
import ConfigParser

CONFIG = ConfigParser.ConfigParser()
CONFIG.read("project.cfg")

class Scheduler(object):
    """Scheduler action"""
    def __init__(self):
        """Constructor"""
        print("foo")
