



from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path
import numpy as np


user = "Ben Knighton"


def PersonVerification(filePath):
    wav = preprocess_wav(filePath)
    embeds_b = encoder.embed_utterance(wav)
    utt_sim_matrix = (np.inner(embeds_a, embeds_b)).item()
    # print("speaker:", utt_sim_matrix)
    if round(utt_sim_matrix, 1) > float(verification_threshold_regression):
        return user
    else:
        return "Unknown"

encoder = VoiceEncoder()
fpath = Path("test2.wav")
p_wav = preprocess_wav(fpath)
embeds_a = encoder.embed_utterance(p_wav)

verification_threshold_regression = 0.60



speaker_rotation = PersonVerification('ending.wav')
print(speaker_rotation)

