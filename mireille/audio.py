"""Class example"""
from sys import byteorder
from array import array
from struct import pack
import ConfigParser
import wave
import pyaudio

CONFIG = ConfigParser.ConfigParser()
CONFIG.read("mireille.cfg")

def normalize(snd_data):
    """Average the volume out"""
    _max = 16384
    times = float(_max)/max(abs(i) for i in snd_data)

    _buffer = array('h')
    for i in snd_data:
        _buffer.append(int(i*times))
    return _buffer

class Audio(object):
    """Scheduler action"""
    def __init__(self):
        """Constructor"""
        self._threshold = int(CONFIG.get('audio', 'threshold'))
        self._chunk_size = int(CONFIG.get('audio', 'chunk_size'))
        self._format = pyaudio.paInt16
        self._bufferate = int(CONFIG.get('audio', 'rate'))

    def is_silent(self, snd_data):
        """Returns 'True' if below the 'silent' self._threshold"""
        return max(snd_data) < self._threshold

    def trim(self, snd_data):
        "Trim the blank spots at the start and end"
        def _trim(snd_data):
            snd_started = False
            _buffer = array('h')

            for i in snd_data:
                if not snd_started and abs(i) > self._threshold:
                    snd_started = True
                    _buffer.append(i)

                elif snd_started:
                    _buffer.append(i)
            return _buffer

        # Trim to the left
        snd_data = _trim(snd_data)

        # Trim to the right
        snd_data.reverse()
        snd_data = _trim(snd_data)
        snd_data.reverse()
        return snd_data

    def add_silence(self, snd_data, seconds):
        """Add silence to the start and end of 'snd_data' of length 'seconds'
        (float)"""
        _buffer = array('h', [0 for i in xrange(int(seconds*self._bufferate))])
        _buffer.extend(snd_data)
        _buffer.extend([0 for i in xrange(int(seconds*self._bufferate))])
        return _buffer

    def record(self):
        """
        Record a word or words from the microphone and
        return the data as an array of signed shorts.

        Normalizes the audio, trims silence from the
        start and end, and pads with 0.5 seconds of
        blank sound to make sure VLC et al can play
        it without getting chopped off.
        """
        _pyaudio = pyaudio.PyAudio()
        stream = _pyaudio.open(format=self._format, channels=1,
                               rate=self._bufferate,
                               input=True, output=True,
                               frames_pyaudioer_buffer=self._chunk_size)

        num_silent = 0
        snd_started = False

        _buffer = array('h')

        while 1:
            # little endian, signed short
            snd_data = array('h', stream.read(self._chunk_size))
            if byteorder == 'big':
                snd_data.byteswap()
            _buffer.extend(snd_data)

            silent = self.is_silent(snd_data)

            if silent and snd_started:
                num_silent += 1
            elif not silent and not snd_started:
                snd_started = True

            if snd_started and num_silent > 30:
                break

        sample_width = _pyaudio.get_sample_size(self._format)
        stream.stop_stream()
        stream.close()
        _pyaudio.terminate()

        _buffer = normalize(_buffer)
        _buffer = self.trim(_buffer)
        _buffer = self.add_silence(_buffer, 0.5)
        return sample_width, _buffer

    def record_to_file(self, path):
        "Records from the microphone and outputs the resulting data to 'path'"
        sample_width, data = self.record()
        data = pack('<' + ('h'*len(data)), *data)

        _wf = wave.open(path, 'wb')
        _wf.setnchannels(1)
        _wf.setsampwidth(sample_width)
        _wf.setframerate(self._bufferate)
        _wf.writeframes(data)
        _wf.close()
