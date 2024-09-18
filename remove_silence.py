import argparse
from pydub import AudioSegment
from pydub.silence import split_on_silence

def remove_silence(input_file, output_file, min_silence_len=1000, silence_thresh=-50):
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove silence from MP3 files")
    parser.add_argument("input_file", help="Path to the input MP3 file")
    parser.add_argument("output_file", help="Path to the output MP3 file")
    parser.add_argument("--min_silence_len", type=int, default=1000, help="Minimum length of silence (in ms) to be removed")
    parser.add_argument("--silence_thresh", type=int, default=-50, help="Silence threshold in dB")
    
    args = parser.parse_args()
    
    remove_silence(args.input_file, args.output_file, args.min_silence_len, args.silence_thresh)
    print(f"Processed {args.input_file} and saved result to {args.output_file}")
