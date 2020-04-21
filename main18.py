import requests
import json

s = requests.Session()

url = 'https://api.bytehand.com/v2/sms/messages'

head = {'Content-Type': 'application/json;charset=UTF-8', 
        'X-Service-Key': '6kXimNjLh3XH2MBEhtTrgqwSSWmkmHs4'}  
  
#data = '{"Language":"ru"}{"Params":[null, null, 1, null, null]}{"V":1}{"Adult": false}'
d= {"sender": "test","receiver": "79625985891","text": "It is testing"}



res = s.post(url, data=json.dumps(d), headers=head)




#response = requests.get('http://pythontest.uxp.ru')
#print(response.content)
#response.json()
#response.headers
#response.headers.get('Server')


#X-Service-Key
#X-Service-Key: 6kXimNjLh3XH2MBEhtTrgqwSSWmkmHs4
#https://api.bytehand.com/v2/oauth/token?code=x3MwNSEPLW2PnAnWCbLdRevprwegQ0KhrcifmZk3NqZwhVdJ6Hg81yR8tZUjNIAw&client_secret=6kXimNjLh3XH2MBEhtTrgqwSSWmkmHs4&client_id=41667&redirect_uri=https%3A%2F%2Fsomewhere.com%2Fcallback&grant_type=authorization_code