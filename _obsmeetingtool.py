#!/usr/bin/python
# Authored By Sciiiman (Github: T-EV)
# MIT License
import whisper
import argparse
import ffmpeg
from timeit import default_timer as timer
import glob
import os

def processVideo(video):
    try:
        stream = ffmpeg.input(video)
        audio = video[0:-3]+'mp3'
        stream = ffmpeg.output(stream, audio, **{'b:a': "96k"})
        ffmpeg.overwrite_output(stream)
        ffmpeg.run(stream)
        return audio
    except:
        return "failed.mp3"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("audio", nargs='?', help="Path to your audio or video file... Use tab complete", type=str)
    parser.add_argument("lang", nargs='?', help="english (Default), spanish, german, portuguese, japanese, italian, russian, polish, french (Langs GPU only)/nFULL LIST: https://github.com/openai/whisper/raw/main/language-breakdown.svg", type=str)
    args = parser.parse_args()

    #if no file sent grab the most recent file in the folder
    if args.audio is None:
        list_of_files = glob.glob('./*.mp4') # * means all if need specific format then *.csv
        if len(list_of_files) == 0:
            print("AAAH THERE IS NO NEW MP4 FILES... I QUIT")
            return
        args.audio = max(list_of_files, key=os.path.getctime)
        #latest_files = list_of_files.sort(reverse=True, key=os.path.getctime)
        
    
    #Figure out if we need to convert the file by looking at the extension
    if args.audio.find(".mp4")==-1:
        audio = args.audio
    else:
        start = timer()
        audio = processVideo(args.audio)
        print(f"==============================================================\nAUDIO CONVERSION COMPLETE ({round(timer() - start)}s)... Working on transcript\n==============================================================")
    
    #Load AI appropriate for system requirements
    model = whisper.load_model("tiny")
    print(f"GPU vs CPU Setup: { model.device.type} setup detected")
    if(model.device.type == "cpu"):
        print("===========================\nOptimizing AI... Results might not be as accurate\nTry running this on a computer with a GPU next time! It is WAAAY Faster\n===========================\n")
    else:
        print("loading bigger model")
        model = whisper.load_model("base")

    #Begin transcription
    print(f"Processing File: {audio}\n...\n Creating Transcript File...")
    start = timer()
    og_result = model.transcribe(audio)["text"]
    result = og_result.replace(".", "\n\n")
    print(result)
    print(f"English Transcription Duration: {timer() - start}s")

    #Write transcript to text file
    text_file = open(audio[0:-4]+"_transcript.txt", "w")
    n = text_file.write(result)
    text_file.close()
    print("Transcript created. Conversion Success!")

    #Check if translation was requested
    if args.lang is not None and model.device.type != "cpu":
        print("Translating")
        args.lang = args.lang.lower()
        #Begin Translation
        try:
            start = timer()
            translated = model.transcribe(audio, language=args.lang)["text"]
            print(translated)
            print(f"Translated Transcription Duration: {timer() - start}s")
        except:
            print("This Language Isn't Supported")
            return
        if len(translated)==0:
            print("Welp... I tried but my brain is too smol. Make my brain bigger and I might have an answer!")
        else:
            #Write translated transcript to text file
            text_file = open(audio[0:-4]+"_transcript_"+args.lang+".txt", "w")
            n = text_file.write(translated)
            text_file.close()
            print(args.lang+" Transcript created. Conversion Success!")


if __name__ == "__main__":
    main()
