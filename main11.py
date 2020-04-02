import vk_api

vk_session = vk_api.VkApi('+79625985891', 'pass')
vk_session.auth()

vk = vk_session.get_api()

print(vk.wall.post(message='Hello world!'))