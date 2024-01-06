from os import getenv, path
from dotenv import load_dotenv
import json

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

YOUTUBE_CHANELS = json.loads(getenv("YOUTUBE_CHANELS"))
VIDEO_PATH_DIR = getenv("VIDEO_PATH_DIR")

CLEANUP_DATA = False