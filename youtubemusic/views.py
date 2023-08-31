import os
import subprocess
import youtube_dl
from django.http import JsonResponse
import vlc
from django.http import HttpResponse
from django.conf import settings
import json
from django.http import JsonResponse
from ytmusicapi import YTMusic
from youtubemusic.firebaseFucntions import add_song
BASE_DIR = settings.BASE_DIR
def getHome(request):
    print("here for Home Page")
    yt= YTMusic()
    results = yt.get_home(5)
    return HttpResponse(json.dumps(results))

def searchsong(request):
    print("here for song search")
    video_url = request.GET.get('list_url')
    
    yt= YTMusic()
    results = yt.search(video_url,filter='songs')
    # print(json.dumps(results))
    return HttpResponse(json.dumps(results))
def getPlay(request):
    print("here for playlist")
    video_url = request.GET.get('list_url')
    # ydl_opts = {
    #     'format': 'bestaudio/best',
    #     'getthumbnail': True,
    #     'verbose':True,
    #     'outtmpl': './downloads/%(id)s.%(ext)s',
    #     'postprocessors': [{
    #         'key': 'FFmpegExtractAudio',
    #         'preferredcodec': 'm4a',
    #         'preferredquality': '320',
    #     }],
    # }
    ydl_opts = {
        "flatplaylist":True,
        "dumpjson":True,
        
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url,  download=False)
        print(info)
        return HttpResponse('info')
        # add_song(datajson)
def get_info(request):
    video_url = request.GET.get('video_url')
    ydl_opts = {
        'format': 'bestaudio/best',
        'getthumbnail': True,
        'verbose':True,
        'outtmpl': './downloads/%(id)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': '320',
        }],
    }
   

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        print(info['creator'])
        thumbnail_url = info['thumbnail']
        # ydl.download([video_url])
        datajson = {
            'url':info['url'],
            'vid':info['id'],
            'title':info['title'],
            'thumb':thumbnail_url,
            'duration':info['duration'],
            'artist':info['artist'].split(',')[0]
        }
        json_data = json.dumps(datajson)
        return HttpResponse(json_data)
        # add_song(datajson)

        
    
def down_song(request):
    video_url = request.GET.get('video_url')
    ydl_opts = {
        'format': 'bestaudio/best',
        'getthumbnail': True,
        'verbose':True,
        'outtmpl': './downloads/%(id)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': '320',
        }],
    }


    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        # print(info)
        # save_json_to_file(info,'data.txt')
        thumbnail_url = info['thumbnail']
        songpath = './downloads/'+info['id']+'.m4a'
        if os.path.exists(songpath):
            print("File exists!")
        else:
            ydl.download([video_url])
        datajson = {
            'url':info['url'],
            'vid':info['id'],
            'title':info['title'],
            'thumb':thumbnail_url,
            'duration':info['duration']
        }
        json_data = json.dumps(datajson)
        add_song(datajson)
        return HttpResponse(json_data)
        
    
    # return HttpResponse('datajson')

def save_json_to_file(json_data, file_path):
    with open(file_path, 'w') as file:
        file.write(str(json_data))

