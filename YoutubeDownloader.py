#!/usr/bin/env python3

import pytube
from pytube import YouTube
import os.path
path = os.path.expanduser("~")
video_link = input("Please enter the youtube video url : ")
resulution = input("Enter the resultion you want 144,240, 360 , 480 , 720 : ")
while len(resulution)<3:
    print("please enter a valid number ")
    resulution = input("Enter the resultion you want 144, 240, 360 , 480 , 720 : ")

print("The Video is being downloading now please wait .....")

res = resulution+'p'
video = YouTube(video_link)
video.streams.filter(res=res).first().download(path)
print(f"\nThe videos was saved in {path}")
