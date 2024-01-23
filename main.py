import librosa
import numpy as np
from notes import *

# File path to your very isolated and lonely vocals file
filePathIsolated = "output_directory/backtoblack/vocals.wav"
pitchArr = []

def dominantPitch(filePath, offset, duration):
    y, sr = librosa.load(filePath, offset=offset, duration=duration)
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

    def extractDominantPitch(pitches, magnitudes):
        indexOfMaxMagnitudes = np.argmax(magnitudes, axis=0)
        dominantPitches = pitches[indexOfMaxMagnitudes, range(pitches.shape[1])]
        dominantPitch = np.median(dominantPitches[dominantPitches > 0])
        return dominantPitch

    dominantPitch = extractDominantPitch(pitches, magnitudes)
    return dominantPitch

def length(filePath):
    y, sr = librosa.load(filePath, sr=None)
    return len(y) / sr

def main():
    for i in range(2, int(length(filePathIsolated)) + 1):
        curPitch = dominantPitch(filePathIsolated, i - 1, i)
        pitchArr.append(curPitch)
      
    # Print the notes for each pitch, maybe not so very muchos necessary but nice to see
    for i, pitch in enumerate(pitchArr):
      closestPitch = min(pitches.items(), key = lambda x: abs(x[1] - pitch))[0]
      print(closestPitch)

if __name__ == "__main__":
    main()