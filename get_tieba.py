import urllib
import re

__metaclass__ = type

class xiazaiImg:

	def GetHtml(self, url):
		global url1
		self.url = url
		urlno = 1
		baiduurl = url + str(urlno)
		url1 = urllib.urlopen(baiduurl).read()

	def GetImg(self, html):
		pat = ('src=\"(.*?\.jpg)\".pic_ext')
		mat = re.compile(pat)
		imgs = re.findall(mat, url1)
		x = 1
		for a in imgs:
			urllib.urlretrieve(a, '%s.jpg' % x)
			print "downloading No.%r" % x
			x +=1
class xiazaiImg2(xiazaiImg):
	def GetHtml(self, url3):
		global url2
		self.url3 = url3
		urlno1 = 1
		while urlno1 < 11:
			urlno1 +=1
			baiduurl = url3 + str(urlno1)
			url2 = urllib.urlopen(baiduurl).read()

	def GetImg(self, html):
		pat = ('src=\"(.*?\.jpg)\".pic_ext')
		mat = re.compile(pat)
		imgs = re.findall(mat, url2)
		x1 = 4
		for a in imgs:
			urllib.urlretrieve(a, '%s.jpg' % x1)
			print "downloading No.%r" % x1
			x1 +=1		

print '#' * 30
print 'Baidu Tieba jpg Downloader'
print 'Enter url of someone page'
print '#' * 30
download1 = raw_input("Enter some url of page in Tieba: ")
html = xiazaiImg()
html1 = html.GetHtml('download1')
html2 = html.GetImg(html1)
html3 = xiazaiImg2()
html4 = html3.GetHtml('download1')
html5 = html3.GetImg(html4)
