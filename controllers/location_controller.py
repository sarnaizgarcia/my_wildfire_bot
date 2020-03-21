from errors.errors import NotCorrectFormatError
from facade.location_params_facade import location_params_facade
from services.image_handler import images_handler


def location_ctnl(params):
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
    # except Exception:
    #     return {
    #         'message': 'There has been an error',
    #         'status': 500

    #     }
