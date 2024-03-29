import os
import cv2
import numpy as np
import datetime
from ipywidgets import Output, Button, Layout, HBox, widgets
from IPython.display import Image, display, clear_output

LABELS_DICT = {}
click_flag = False
video = cv2.VideoCapture("carol4.mp4")

frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
fps = video.get(cv2.CAP_PROP_FPS)
seconds = round(frames / fps)
video_time = datetime.timedelta(seconds=seconds)
print(f"duration of video in seconds: {seconds}")

frame_id = 700
while frame_id < (frames - fps):
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
    ret, frame = video.read()
    cv2.imwrite("/content/frame_test/frame%d.jpg" % frame_id, frame)
    frame_id += int(fps)
    
    
def on_button_clicked(b):
    global click_flag
    with output:
        click_flag = True
    add_label(filename[5:-4], b.description)


def add_label(frame, label):
    global LABELS_DICT
    LABELS_DICT[frame] = label


def next_frame(b):
    global flag
    with output:
        clear_output(wait=True)
    flag = True
  
  
directory = "/content/frame_test"
flag = True

for filename in os.listdir(directory)[:1]:
    while flag:
        click_flag = False
        flag = False
        f = os.path.join(directory, filename)
        yes_button = widgets.Button(description = "Yes")
        no_button = widgets.Button(description = "No")
        next_button = widgets.Button(description = "Next")
        output = widgets.Output(layout=Layout(width='50%', height='50%'))
        if os.path.isfile(f) and not filename.endswith(".DS_Store"):
            image = Image(f, width='600', height='300')
            print('\nFigure number:', filename[5:-4])
            print('Is ____ talking in this specific frame?','\n')
            yes_button.on_click(on_button_clicked)
            no_button.on_click(on_button_clicked)
            next_button.on_click(next_frame)


            display(yes_button, no_button, output, next_button, image)
