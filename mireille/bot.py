"""Bot class"""
import ConfigParser
import glob

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from bs4 import BeautifulSoup
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
    def train(data):
        """Traine the bot"""
        bot = ChatBot(CONFIG.get('general', 'botname'))
        bot.set_trainer(ListTrainer)
        # Train based on the english corpus
        bot.train(data)
        # Get a response to an input statement
        bot.get_response("Salut !")

    def extract_corpus_from_epub(self, path):
        """Extract data from corpus"""
        _data = []
        for _file in glob.glob(path):
            soup = BeautifulSoup(open(_file), 'html.parser')
            for sentence in soup.find_all('p','MsoNormal'):
                if sentence.string is not None:
                    if not sentence.string.isupper():
                        _data.extend(sentence.string.replace("\n"," "))
        self.train(_data)
