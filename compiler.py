from moviepy.editor import *

def compile_clips():
    # Open video file
    clip = VideoFileClip("example.mp4")
    times = find_death_times(clip)

    clips = []


def find_death_times(clip):
    time_stamp = 0
    death_times = []

    while time_stamp < clip.duration:
        frame = clip.get_frame(time_stamp)
        print "time: " + str(time_stamp)

        if is_you_died(frame):
            print "death at: " + str(time_stamp)
            death_times.append(time_stamp)

        time_stamp += 1.0
    return death_times

locations_to_check = [(436, 372),(476, 370),(558, 361),(657, 360),
    (436, 372),(733, 368),(762, 358),(821, 360)]

def is_you_died(frame):
    color_checks = []
    for location in locations_to_check:
        color_checks.append(is_red(frame[location[1],location[0]]))

    num_true = 0
    for check_bool in color_checks:
        if check_bool:
            num_true += 1

    print num_true

    if num_true > 0:
        return True
    else:
        return False

def is_red(color):
    return color[0] >= 60 and color[1] <= 10 and color[2] <= 20

find_death_times()
