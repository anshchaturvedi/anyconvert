import os
import pydub
import time
import threading

# Function to process a single file
def process_file(file_name):
    tic = time.perf_counter()
    print(f"Extracting sound from {file_name}.wav...")
    sound = pydub.AudioSegment.from_wav(f"{file_name}.wav")
    print("Extracted sound. Exporting to mp3...")
    sound.export(f"{file_name}.mp3", format="mp3")
    toc = time.perf_counter()
    print(f"Exported sound as {file_name}.mp3, took {toc - tic:0.4f} seconds.")
    print()

res = []

for file in os.listdir("/Users/anshchaturvedi/Documents/wav files"):
    if file.endswith('.wav'):
        res.append(file)

files = [os.path.splitext(file)[0] for file in res]

# Create and start a thread for each file
threads = []
for file_name in files:
    thread = threading.Thread(target=process_file, args=(file_name,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All tasks completed.")
