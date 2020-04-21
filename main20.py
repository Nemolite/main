import vk_api

vk_session = vk_api.VkApi('номер', 'пароль')
vk_session.auth()

vk = vk_session.get_api()

posts = vk.wall.get(count=1000)['items'] 
while(posts):
	for post in posts:
		print(post['id'])
		vk.wall.delete(post_id=post['id'])


                    
        
        

