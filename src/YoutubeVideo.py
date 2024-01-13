import scrapetube
from pytube import YouTube
from loger import LOGGER
from env import VIDEO_PATH_DIR

class YoutubeVideo:
    def __init__(self,channelusername):
        self.channelusername = channelusername
        self.currentlastedvideoid = self.getvideoid()['videoId']

    def getvideoid(self):
        try:
            videos = scrapetube.get_channel(channel_username = self.channelusername, limit = 1, sort_by = "newest")
            return next(videos)
        except Exception as e:      
            LOGGER.error("Faild to get youtube video id ",e)
    
    def downloadytvideo(self,lastedvideo):
        try:
            youtubeObject = YouTube(f"https://www.youtube.com/watch?v={ lastedvideo['videoId'] }")
            youtubeObject = youtubeObject.streams.get_by_resolution("720p")
            youtubeObject.download(filename=f'{ self.channelusername }.mp4', output_path=VIDEO_PATH_DIR, skip_existing=False)
        except Exception as e:
            LOGGER.error(f"Fail to download video '{ lastedvideo['videoId'] }' from chanel { self.channelusername } ",e)
            return
        self.currentlastedvideoid = lastedvideo['videoId']
        LOGGER.success(f"Succesfully downloaded video '{ lastedvideo['videoId'] }' from chanel { self.channelusername }")

    def searchanddownload(self):
        lastedvideo =  self.getvideoid()
        if self.currentlastedvideoid != lastedvideo['videoId']:
            LOGGER.info(f"Newest video on chanel { self.channelusername } detected starting donwload")
            self.downloadytvideo(lastedvideo)
        else:
            LOGGER.info(f"Newest video on chanel { self.channelusername } not detected")