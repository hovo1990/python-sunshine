# TODO this works, but also captures microphone
import sounddevice as sd
from scipy.io.wavfile import write
# python -m sounddevice to know all stuff

fs = 300100  # Sample rate
seconds = 30  # Duration of recording
# sd.default.device = 'default'  # Speakers full name here
sd.default.device = 1 # Speakers full name here

# myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)  # Save as WAV file