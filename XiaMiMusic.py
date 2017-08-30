#coding=utf-8

import urllib, urllib2
import json


###################################
#
#       查询歌曲资源的位置信息
#       其中keyword设置查询关键字
#       返回sourceUrl
#       注意需要设定headers，否则会被拒绝访问
#
###################################

keyword = "神秘嘉宾"
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    'Referer':'http://m.xiami.com/'
}
queryFileUrl = 'http://api.xiami.com/web?v=2.0&app_key=1&key=' + keyword + '&page=1&limit=50&callback=jsonp154&r=search/songs';
request = urllib2.Request(queryFileUrl, headers=headers)
responseInfo = urllib2.urlopen(request)
jsonInfo = json.loads(responseInfo.read()[9:-1])

for song in list(jsonInfo["data"]["songs"]):
    if song["song_name"] == keyword.decode("utf-8"):
        sourceUrl = song["listen_file"]
        break;
    else:
        sourceUrl = None


###################################
#
#       获取歌曲资源
#
###################################


if sourceUrl is None:
    print "无匹配资源"
    exit()
sourceRequest = urllib2.Request(sourceUrl)
source = urllib2.urlopen(sourceRequest)

with open("神秘嘉宾.mp3","wb") as songHandler:
    songHandler.write(source.read())
