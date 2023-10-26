import argparse
from file_handler import copy_files
from transcriber import transcribe_files
import os

def show_notification(title, message):
    os.system(f"osascript -e 'display notification \"{message}\" with title \"{title}\"'")

def main():
    try:
        parser = argparse.ArgumentParser(description='Backup and transcribe audio files.')
        parser.add_argument('input_dir', type=str, help='The directory containing the audio files to backup and transcribe.')
        parser.add_argument('output_dir', type=str, help='The directory where the backed up files and transcripts will be stored.')
        args = parser.parse_args()

        # Copy files
        new_files = copy_files(args.input_dir, args.output_dir)

        # Transcribe files
        transcribe_files(new_files)
    except Exception as e:
        show_notification("Error", e)        

if __name__ == "__main__":
    main()
