from vkuser import VkUser
from yauploader import YaUploader

if __name__ == '__main__':
    yandex_token = ''

    uploader = YaUploader(yandex_token)
    vk_user = VkUser('552934290')
    uploader.upload_photo_from_vk(vk_user)

