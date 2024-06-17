import os
import shutil
from datetime import datetime

audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

txt = (".txt", ".pdf", ".doc")

code =(".py", ".php", ".html", ".css", ".cpp", ".js")

def is_text(file):
    return os.path.splitext(file)[1] in txt

def is_code(file):
    return os.path.splitext(file)[1] in code

def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_image(file):
    return os.path.splitext(file)[1] in img

def is_screenshot(file):
    name, ext = os.path.splitext(file)
    return (ext in img) and "screenshot" in name.lower()

os.chdir("/GenFolder/Downloads/File Organizer")

for file in os.listdir():
    if is_audio(file):
        dst = "/GenFolder/Downloads/File Organizer/data/audio"
    elif is_video(file):
        dst = "/GenFolder/Downloads/File Organizer/data/video"
    elif is_text(file):
        dst = "/GenFolder/Downloads/File Organizer/data/text"
    elif is_code(file):
        dst = "/GenFolder/Downloads/File Organizer/data/code"
    elif is_image(file):
        if is_screenshot(file):
            dst = "/GenFolder/Downloads/File Organizer/data/screenshots"
        else:
            dst = "/GenFolder/Downloads/File Organizer/data/images"
    else:
        dst = "/GenFolder/Downloads/File Organizer/data"

    if os.path.isfile(file): 
        filename, file_extension = os.path.splitext(file)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        new_filename = f"{filename}_{timestamp}{file_extension}"
        shutil.move(file, os.path.join(dst, new_filename))
    else:
        print(f"{file} is not a valid file.")
