#!bot/bin/python3
# pylint: disable=C0103
# -*- coding: utf-8 -*-
import io
import os
import time
import ConfigParser
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

CONFIG = ConfigParser.ConfigParser()
CONFIG.read("mireille.cfg")

class Speech(object):

    def get_words(self, sound_file):
        # Instantiates a client
        client = speech.SpeechClient()
        # Loads the audio into memory
        with io.open(sound_file, 'rb') as audio_file:
            content = audio_file.read()
            audio = types.RecognitionAudio(content=content)

        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code='fr-FR')

        # Detects speech in the audio file
        response = client.recognize(config, audio)
        if len(response.results) > 0:
            return response.results[0].alternatives[0].transcript
        return None