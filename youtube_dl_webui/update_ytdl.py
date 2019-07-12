import pip
import requests
from youtube_dl import version
from subprocess import call
import time

version_url = "https://raw.githubusercontent.com/ytdl-org/youtube-dl/master/youtube_dl/version.py"

def Check_Version():
    res = requests.get(version_url)
    res.encoding = 'utf-8'
    remote_version = str(res.content).split("'")[-2]
          #.split(r'\n')[-2].split("'")[1])
    youtube_dl_version = version.__version__
    if remote_version != youtube_dl_version:
        call("pip install --upgrade " + "youtube-dl", shell=True)



def print_test():
    print(time.time())