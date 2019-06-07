import os
from moviepy.editor import VideoFileClip
from pathlib import Path

p=Path(input()).resolve()
p=str(p)
os.chdir(p)


total=0


if os.path.isdir(p):
    for root,dirs,files in os.walk(p):
        for file in files:
            if file.endswith('.mp4'):
                try:
                    clip = VideoFileClip(os.path.join(root,file))
                    total+= clip.duration
                    clip.reader.close()
                    clip.audio.reader.close_proc()
                except:
                    print("Invalid File"+file)
else:
    print("path was not found")
print(total)


