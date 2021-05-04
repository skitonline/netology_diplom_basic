from vkuser import VkUser
from yauploader import YaUploader

if __name__ == '__main__':
    token = ''

    uploader = YaUploader(token)
    vk_user = VkUser('552934290')
    uploader.upload_photo_from_vk(vk_user)

