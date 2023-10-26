# auto-audio-note
Turn recording devices, such as the DJI Mic, into convenient note-taking gadgets. 

Keep your ideas and thoughts simply by talking instead of interacting with your phone or computer, reducing the possibility of getting distracted.

Utilize [openai/whisper](https://github.com/openai/whisper) to do speech to text. And uses a hammerspoon script to initiate ASR and keep files ordered by date. 

## Work Flow
1. Record on a device
2. Plug it in to the computer
3. Script automatically starts and start trancribing
4. Text files generated in the output folder

## Setup
1. Recording device
![b3b8a6a76cff006e5fc29a3ed542d41f](https://github.com/JoeyWangTW/auto-audio-note/assets/11681724/74e80ee9-adf2-400c-8221-f25ce48861e5)
I happen to have a DJI mic. It is small and compact, very easy to use with good audio quality.

2. Setup Python Environment
Clone repo
```
git clone https://github.com/JoeyWangTW/auto-audio-note.git
cd auto-audio-note
```
Setup virtual environment
```
# make sure you have python3.8+ to use whisper
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Edit `run.sh` for your own input output path
4. Add hammerspoon lua script from `usb-watcher.lua`

## Limitations
- It's using whisper "small" model, takes quite some time to transcribe. However, I find it have better multi-language performance.
- Only WAV files are allowed
- Progress is not very visible

## Next steps
- Add to obsidian daily journal automatically
- Support settings and make choosing input/output path easier
