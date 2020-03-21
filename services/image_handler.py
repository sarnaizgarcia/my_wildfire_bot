import os

from nasa import earth

from entities.image import Image


os.environ.setdefault(
    'NASA_API_KEY',
    '7POab3qBGpcqDqGUocE1huTPaeiBPGAaM09znaMb',
)

MAX_CLOUD_SCORE = 0.5


class ImagesHandler:
    def __init__(self):
        self.index = 0
        self.image_list = list()

    def create_list(self, lon, lat, begin, end):
        assets = earth.assets(lon=lon, lat=lat, begin=begin, end=end)

        for asset in assets:
            img = asset.get_asset_image(cloud_score=True)

            if (img.cloud_score or 1.0) <= MAX_CLOUD_SCORE:
                self.image_list.append(Image(asset, img))

    def index_image(self):
        return self.image_list[self.index][1]

    def increase_index(self):
        self.index += 1

    def get_date(self):
        return self.image_list[self.index][0].date

    def get_length(self):
        return len(self.image_list)


images_handler = ImagesHandler()
