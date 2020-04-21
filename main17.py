import urllib.request
response = urllib.request.urlopen('https://www.bytehand.com/')
print(response)
print(response.getheader('Server'))
print(response.getcode())

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
print(password_mgr)
#top_level_url = 'https://api.bytehand.com/v2/users'
#password_mgr.add_password(None, top_level_url, 'G16052015@MAIL.RU', 'QAZwsx!@#456')
#handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
#opener = urllib.request.build_opener(handler)
#response = opener.open(top_level_url)
#response.getcode()


