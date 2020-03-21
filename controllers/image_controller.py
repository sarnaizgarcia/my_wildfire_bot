import json

import traceback
from services.image_handler import images_handler


def image_controller():
    try:
        image = images_handler.index_image()

        response = {
            'message': json.dumps({
                'cloud_score': image.cloud_score,
                'date': image.date,
                'id': image.id,
                'resource': {
                    'dataset': image.resource['dataset'],
                    'planet': image.resource['planet']
                },
                'url': image.url
            }),
            'status': 200
        }
        return response

    except Exception:
        print(traceback.format_exc())
        return {
            'message': 'There has been an error',
            'status': 500
        }
