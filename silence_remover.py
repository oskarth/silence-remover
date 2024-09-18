#!/usr/bin/env python3

import argparse
import os
import sys
from pydub import AudioSegment
from pydub.silence import split_on_silence
import multiprocessing

def process_file(input_file, output_file, min_silence_len, silence_thresh):
    """Process a single MP3 file to remove silence."""
    print(f"Processing {input_file}")
    sys.stdout.flush()
    
    # Load the audio file
    audio = AudioSegment.from_mp3(input_file)
    
    # Split the audio into non-silent chunks
    chunks = split_on_silence(
        audio,
        min_silence_len=min_silence_len,
        silence_thresh=silence_thresh
    )
    
    # Concatenate the non-silent chunks
    output_audio = AudioSegment.empty()
    for chunk in chunks:
        output_audio += chunk
    
    # Export the result
    output_audio.export(output_file, format="mp3")

def remove_silence(input_path, output_path, min_silence_len=1000, silence_thresh=-50):
    """Remove silence from MP3 file(s) in the input path and save to the output path."""
    if os.path.isfile(input_path):
        # Process a single file
        process_file(input_path, output_path, min_silence_len, silence_thresh)
    elif os.path.isdir(input_path):
        # Process a directory of files
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Prepare list of files to process
        files_to_process = []
        for filename in os.listdir(input_path):
            if filename.endswith(".mp3"):
                input_file = os.path.join(input_path, filename)
                output_file = os.path.join(output_path, filename)
                files_to_process.append((input_file, output_file, min_silence_len, silence_thresh))

        # Use multiprocessing to process files in parallel
        with multiprocessing.Pool() as pool:
            pool.starmap(process_file, files_to_process)
    else:
        print(f"Error: {input_path} is not a valid file or directory", file=sys.stderr)

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Remove silence from MP3 files or folders")
    parser.add_argument("input_path", help="Path to the input MP3 file or folder")
    parser.add_argument("output_path", help="Path to the output MP3 file or folder")
    parser.add_argument("--min_silence_len", type=int, default=1000, help="Minimum length of silence (in ms) to be removed")
    parser.add_argument("--silence_thresh", type=int, default=-50, help="Silence threshold in dB")
    
    args = parser.parse_args()
    
    # Run the silence removal process
    remove_silence(args.input_path, args.output_path, args.min_silence_len, args.silence_thresh)
    print("Processing complete.")