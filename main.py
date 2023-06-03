import os
import random
import datetime
from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo
import sys

# program_out = open("test.out", 'w')
# sys.stdout = program_out

channel = Channel()
channel.login("client-secret.json", "credentials.storage")

#media directrory 
path = 'instaloader/test'


def filehandler():
    mp4_files = [f for f in os.listdir(path) if f.endswith(".mp4")]
    random_file = random.choice(mp4_files)
    return random_file


def captionfile(name:str):
    with open(os.path.join(path, name), encoding="utf-8") as f:
        lines = f.readlines()
    return lines

def delete(filename):
    text_file = filename + ".txt"
    mp4 = filename + ".mp4"
    os.remove(os.path.join(path, text_file))
    os.remove(os.path.join(path, mp4))

def uploadvideo(mp4_file:str, title:str, description:str, thumbnail:str, tags):
    #https://pypi.org/project/simple-youtube-api/
    video = LocalVideo(os.path.join(path, mp4_file))

    # setting snippet
    video.set_title(title)
    video.set_description(description)
    video.set_tags(tags)
    #video.set_category("movie")
    video.set_default_language("en-US")

    # setting status
    video.set_embeddable(True)
    video.set_license("creativeCommon")
    video.set_privacy_status("public")
    video.set_public_stats_viewable(True)

    # setting thumbnail
    video.set_thumbnail_path(os.path.join(path, thumbnail))

    # uploading video and printing the results
    video = channel.upload_video(video)
    print(video.id)
    print(video)

    # liking video
    video.like()

file = filehandler()
filename = file.split(".")
mp4_file = str(filename[0])+".mp4"
text_file = str(filename[0])+".txt"
thumbnail = str(filename[0])+".jpg"

print("uploading : ", mp4_file, text_file, thumbnail)

try:
    caption = captionfile(text_file)
except FileNotFoundError:
    caption = "Sample" #give fail save caption 


title = caption[0]
description = ' '.join([item.replace('\n', '') for item in caption])
tags = [item.replace('#', '').replace('\n', '') for item in [i for i in caption if i.startswith('#')]]





uploadvideo(mp4_file, title, description, thumbnail, tags)

#program_out.close()