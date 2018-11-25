import urllib.request

data = urllib.request.urlopen("http://www.runningmanzx.com/shipin/index_23.html").read()

print(data)
