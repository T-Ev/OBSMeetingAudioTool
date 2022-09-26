@echo off
set p=%~dp0
@REM FOR /F "tokens=*" %%g IN ('python --version') do (SET yespy=%%g)
@REM set yespy2= %yespy% 2>&1 | findstr " 3 "
@REM echo hi: %yespy%
@REM EXIT /B
echo Location: %p%
cd /
mkdir _ffmpeg
cd _ffmpeg
curl --location -O https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip
echo Extracting...
powershell.exe -nologo -noprofile -command "& { Add-Type -A 'System.IO.Compression.FileSystem'; [IO.Compression.ZipFile]::ExtractToDirectory('ffmpeg-release-essentials.zip', '.'); }"
ren ffmpeg-5.1.1-essentials_build ffmpeg
echo PLEASE ADD C:\ffmpeg\bin to your PATH Variable
echo Press Space to open path dialog...
pause
rundll32 sysdm.cpl,EditEnvironmentVariables
echo Continue?
pause
del ffmpeg-release-essentials.zip
cd %p%
curl -LJO https://raw.githubusercontent.com/T-Ev/OBSMeetingAudioTool/main/_obsmeetingtool.py
curl -LJO https://raw.githubusercontent.com/T-Ev/OBSMeetingAudioTool/main/requirements.txt
powershell.exe -nologo -noprofile -command "& { cat requirements.txt | xargs -n 1 pip install }"
@REM cat requirements.txt | xargs -n 1 pip install
echo =========================
echo INSTALL OF TOOL COMPLETE!
echo =========================
echo To use your tool simply move the python file into your OBS capture folder or the same folder where the video is you want to convert
echo syntax is:
echo        python _obsmeetingtool.py filename.mp4
echo OR
echo        If you just double click on the script it will convert the most recent video in the folder
pause
del requirements.txt
del installerv1.bat