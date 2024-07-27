import os
import datetime
import time

def getWordCount(file, path):
    wordcount = 0
    file_path = os.path.join(path, file)
    try:
        with open(file_path, "r") as f:
            for line in f:
                wordcount += len(line.lower().split())
    except FileNotFoundError:
        print(f"File {file} not found.")
    return wordcount

def get_file_word_counts(files, path):
    total_wordcount = 0
    for file in files:
        total_wordcount += getWordCount(file, path)
    return total_wordcount

start_time = datetime.datetime(2024, 7, 27, 15, 25, 00)
end_time = datetime.datetime(2024, 7, 27, 16, 30, 00)

path = "/home/lplab/Desktop/220962344/Week1/dir"
files = set(os.listdir(path))

# Initial word count
wordcount = get_file_word_counts(files, path)

while datetime.datetime.now() < end_time:
    curr_files = set(os.listdir(path))

    deleted_files = files - curr_files
    new_files = curr_files - files

    # Update word count for deleted files
    for file in deleted_files:
        wordcount -= getWordCount(file, path)

    # Update word count for new files
    for file in new_files:
        wordcount += getWordCount(file, path)

    # Update the current set of files
    files = curr_files

    print(f"Active files {len(files)} and words {wordcount}")
    time.sleep(1)
