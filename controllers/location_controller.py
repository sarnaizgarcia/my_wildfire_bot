from errors.errors import NotCorrectFormatError, ListIsEmptyError
from facade.location_params_facade import location_params_facade
from services.image_handler import images_handler

import traceback


def location_ctrl(params):
    try:
        if not location_params_facade.location_params_validation(params):
            raise NotCorrectFormatError
        parsed_params = {
            'lon': params.get('longitude'),
            'lat': params.get('latitude'),
            'begin': params.get('begin_date'),
            'end': params.get('end_date')
        }
        images_handler.create_list(**parsed_params)
        if images_handler.get_length() == 0:
            raise ListIsEmptyError

        response = {
            'message': 'List created',
            'status': 200
        }
        return response

    except NotCorrectFormatError:
        return {
            'message': 'The dictionary has no correct format',
            'status': 400
        }
    except ListIsEmptyError:
        return {
            'message': 'There are no images on the list. Try another latitude or longitude.',
            'status': 404
        }
    except Exception:
        print(traceback.format_exc())
        return {
            'message': 'There has been an error',
            'status': 500

        }
