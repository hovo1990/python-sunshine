print('program start 0 -->')
import soundcard as sc
print('program start-->')
# get a list of all speakers:
speakers = sc.all_speakers()
# get the current default speaker on your system:
default_speaker = sc.default_speaker()
# get a list of all microphones:
mics = sc.all_microphones()
# get the current default microphone on your system:
default_mic = sc.default_microphone()



print(speakers)
# # search for a sound card by substring:
# c.get_speaker('Scarlett')
# <Speaker Focusrite Scarlett 2i2 (2 channels)>
# >>> one_mic = sc.get_microphone('Scarlett')
# <Microphone Focusrite Scalett 2i2 (2 channels)>
# # fuzzy-search to get the same results:
# one_speaker = sc.get_speaker('FS2i2')
# one_mic = sc.get_microphone('FS2i2')