import urllib.request
response = urllib.request.urlopen('https://www.bytehand.com/')
print(response)
print(response.getheader('Server'))
print(response.getcode())


