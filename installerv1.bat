@echo off
cd /
mkdir _ffmpeg
cd _ffmpeg
curl -sO 
cat requirements.txt | xargs -n 1 pip install
pause