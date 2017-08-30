#coding=utf-8

import json
import urllib, urllib2
from Encryption import encryptRequest
###########################################
#
#       获取歌曲的id
#       s: 搜索词
#       limit: 返回数量
#       type: 搜索类型；
#           取值意义:
#           1 单曲
#           10 专辑
#           100 歌手
#           1000 歌单
#           1002 用户
#       offset: 偏移数量，用于分页
#
#############################################

queryUrl = "http://music.163.com/api/search/get/"
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
data = {
    's':'停了的钟',
    'limit':1,
    'type':1,
    'offset':0
}

encode_data = urllib.urlencode(data)
request = urllib2.Request(queryUrl,encode_data,headers = headers)
response = urllib2.urlopen(request)
songInfo = json.loads(response.read())
songId = songInfo['result']['songs'][0]['id']


######################################
#
#       获取歌曲的资源地址
#
######################################
targetUrl = 'http://music.163.com/weapi/song/enhance/player/url?csrf_token=';
csrf = '';

dataSrc = {
    "ids": [songId],
    "br": 320000,
    "csrf_token": csrf
}


encode_dataSrc = urllib.urlencode(encryptRequest(dataSrc))
requestSrc = urllib2.Request(targetUrl,encode_dataSrc,headers = headers)
responeSrc = urllib2.urlopen(requestSrc)
songDetail = json.loads(responeSrc.read())
songUrl = songDetail["data"][0]["url"]



######################################
#
#       下载并存储
#
######################################

song = urllib.urlopen(songUrl)
with open("停了的钟.mp3","wb") as songHandler:
    songHandler.write(song.read())
