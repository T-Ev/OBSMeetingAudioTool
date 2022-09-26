# OBSMeetingAudioTool

This tool can sit in your OBS folder and you can use it to easily convert your meeting recording mp4's to compressed mp3's and auto-generate transcript/notes for faster reading.

## Featuring OpenAI's WHISPER AI Transcription Model

OpenAI just released their new Open Source audio transcription model and I got inspired to use it to autogenerate notes from my long-form remote meetings so I can have a written record, and I can catch up on a meeting in minutes vs sifting through 1 hour of audio. Also the transcript is searchable so I can quickly find relavent conversation and topics.

Whisper is said to be state of the art when it comes to transcription and is resilient when faced with accents and poor audio quality.

This tool will run on any machine, but it will downgrade the quality of the transcription results based on your device's specs. For best performance use a PC with dedicated graphics (preferably NVIDIA).

## Audio MP3 Creation

This tool also takes MP4's outputted by OBS (what I usually use to record Discord meetings) and strips the video and compresses the audio file for easy sharing. Currently it is set to compress it to 96k bitrate.

Having it audio only enables me to listen to the meetings in the car, take it with me, and also save a ton of file storage space.

### TODO

It soon will also speed up the audio by 1.2x for easy listening and to again reduce file size.

# Installation

## Prerequisites

Please ensure you have Python 3 installed. You can [download python here](https://www.python.org/downloads/)

Check your version using this terminal command:
`python --version`

## Installer

I created a little bat script to install ffmpeg and the needed depedencies for you.

Simply download the bat file in the releases section and run it!

## Usage

The installer will leave a python file. This is the file you use to run the program.

Methods:

1. You can put this file in your OBS capture folder and when you double click it, it will start converting the most recent video in the folder.

2. Run the script from the command prompt: `python _obsmeetingtool.py my_meeting_vid.mp4`
