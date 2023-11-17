#%%
import librosa
import matplotlib.pyplot as plt
import numpy as np

# Load the audio file
y, sr = librosa.load('test.wav')
# Only take the first 10 seconds
ten_seconds = 10 * sr
y_ten_seconds = y[:ten_seconds]

# Calculate the RMS value for each frame
frame_length = 1024
hop_length = 512
rms = librosa.feature.rms(y=y_ten_seconds, frame_length=frame_length, hop_length=hop_length)[0]

# Convert frame indices to time
frames = range(len(rms))
t = librosa.frames_to_time(frames, sr=sr, hop_length=hop_length)


print(t.tolist())
# Plot
plt.figure(figsize=(14, 5))
plt.plot(t, rms, label='Volume over Time')  # Plot the line
plt.scatter(t, rms, color='red')  # Plot the points
plt.xlabel('Time (s)')
plt.ylabel('Volume (RMS Amplitude)')
plt.title('Volume Over First 10 Seconds')
plt.legend()
plt.show()
# %%
