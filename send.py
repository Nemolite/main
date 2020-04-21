import requests
import urllib
par = {
    'id':'41667',
    'key':'A19F8C9216D34D8B',
    'to':'+79061342117',
    'from':'It is me',
    'text':'Privet'
}
ses = requests.Session()
print(ses)
#send = ses.post('https://api.bytehand.com/v1/send',params=par)
#print(send.text)
