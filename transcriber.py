import os
import whisper

def show_notification(title, message):
    os.system(f"osascript -e 'display notification \"{message}\" with title \"{title}\"'")


def transcribe_files(files):
    total_files = len(files)
    print("Start transcribing "+str(total_files)+" files...")
    for index, (source, target) in enumerate(files, start=1):
        show_notification("Progress Update", f"Transcription completed for file {index} of {total_files}.")
        print("progress: "+str(index)+"/"+str(total_files))
        prompt='請用繁體中文回答'
        model = whisper.load_model("small")
        transcript = model.transcribe(source, fp16=False, language="Chinese", initial_prompt=prompt)["text"]

        # Create the path for the transcript file
        transcript_file = target 

        # Save transcript to the same directory as the original file
        with open(transcript_file, 'w') as f:
            f.write(transcript)
