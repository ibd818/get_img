# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
print '#' * 50
print 'This Program is download jpg in moko. :)'
print 'Enter someone url of channel in moko. like:"http://www.moko.cc/channels/post/23/1.html"'
print 'All jpg of the channel will be download'
print '#' * 50


ChannelUrl = raw_input("Enter url of channel: ")

readChannelUrl = urllib2.urlopen(ChannelUrl).read()
all_html_url = []
imgs = []


def get_html_url(readChannelUrl):
    global all_html_url
    zhengze = 'href=\"/post/(.*?\.html)\"'
    pat = re.compile(zhengze)
    mat = re.findall(pat, readChannelUrl)
    for allurl in mat:
        allurl1 = 'http://www.moko.cc/post/' + str(allurl)
        all_html_url.append(str(allurl1))
        print allurl1, " add."
    file1 = open(r'd:\python27\test\t1.txt', 'w')
    file1.write(str(all_html_url))
    file1.close()
    return all_html_url


def get_html_jpg(all_html_url):
    global imgs
    gg = '<p class=\"picBox\"><img src2=\"(.*?\.jpg)\"'
    ggpat = re.compile(gg)
    x = 1
    for img in all_html_url:
        readall = urllib2.Request(img)
        readallurl = urllib2.urlopen(readall).read()
        mat = re.findall(ggpat, readallurl)

        for ijpg in mat:
            urllib.urlretrieve(ijpg, r'd:\python27\test\%s.jpg' % x)
            print "No.%s is done." % x
            x += 1

        print mat, 'add.'
    file = open(r'd:\python27\test\t.txt', 'w')
    file.write(str(imgs))
    file.close()


get_html_url(readChannelUrl)
get_html_jpg(all_html_url)

print "all imgs is download"
