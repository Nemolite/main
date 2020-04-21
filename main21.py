import vk_api

vk_session = vk_api.VkApi('+79625985891', 'QAZwsx!@#456')
vk_session.auth()

vk = vk_session.get_api()

posts = vk.wall.get(count=100)['items'] 
while(posts):
	for post in posts:
		print(post['id'])
		vk.wall.delete(photo_id=post['id'])

