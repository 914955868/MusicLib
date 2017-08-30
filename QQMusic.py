#coding=utf-8

import urllib, urllib2
import json

###################################
#
#       查询歌曲id信息
#       在QueryUrl中
#       第一行参数设定当前页返回的个数
#       第二行参数设定返回的页数
#       第三行参数设定查询的歌手或歌曲
#
###################################

headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
pageNum = "1"
num = "1"
song = "独家记忆"

queryIdUrl = "http://s.music.qq.com/fcgi-bin/music_search_new_platform?t=0&amp;n="+num+\
           "&aggr=1&cr=1&loginUin=0&format=json&inCharset=GB2312&outCharset=utf-8&notice=0&platform=jqminiframe.json&needNewCode=0&p="+pageNum+\
           "&catZhida=0&remoteplace=sizer.newclient.next_song&w="+song


response = urllib2.urlopen(queryIdUrl)
songInfo = json.loads(response.read())
usefulData = songInfo["data"]["song"]["list"][0]["f"]
songId = usefulData.split('|')[-5]


###################################
#
#       查询歌曲key信息
#       在queryKeyUrl中
#       第一行参数设定当前页返回的个数
#       第二行参数设定返回的页数
#       第三行参数设定查询的歌手或歌曲
#
###################################

queryKeyUrl = "https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?g_tk=5381&jsonpCallback=MusicJsonCallback5412917381164359&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&cid=205361747&callback=MusicJsonCallback5412917381164359&uin=0&songmid=00184ejM4XouuN&"+\
              "filename=C400"+songId+".m4a&guid=2261907170"
responseKey = urllib2.urlopen(queryKeyUrl)

keyInfo = json.loads(responseKey.read()[34:-1])
key = keyInfo["data"]["items"][0]["vkey"]


###################################
#
#       获取歌曲资源
#       在sourceUrl中
#       第一个参数为songId
#       第二个参数为key
#
###################################

sourceUrl = "http://dl.stream.qqmusic.qq.com/C400"+songId+".m4a?vkey="+key+"&guid=2261907170&uin=0&fromtag=66"

source = urllib2.urlopen(sourceUrl)
with open("独家记忆.mp4","wb") as musicHandler:
    musicHandler.write(source.read())
