from moviepy.editor import *

 # Open video file
clip = VideoFileClip("example.mp4")
time_stamp = 0


while time_stamp < clip.duration:
    clip.get_frame(time_stamp, interactive = True)


    time_stamp += 2.0

def is_you_died(frame):
    is_red()

def is_red(r,g,b):
    return r >= 60 and g <= 10 and b <= 20
