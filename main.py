import schedule
import time
import os
from env import YOUTUBE_CHANELS,VIDEO_PATH_DIR
from src import YoutubeVideo

if not os.path.exists(VIDEO_PATH_DIR):
   os.makedirs(VIDEO_PATH_DIR)

subscribedChanelList = []

for chanel in YOUTUBE_CHANELS:
    subscribedChanelList.append(YoutubeVideo.YoutubeVideo(chanel))

def main(): 
    for chanel in subscribedChanelList:
        chanel.searchanddownload()

schedule.every(20).minutes.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)