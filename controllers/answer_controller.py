import traceback

from errors.errors import BadRequestError
from facade.answer_facade import answer_validator
from services.image_handler import images_handler


def answer_controller(answer_dict):
    try:
        if answer_validator.validate_answer(answer_dict):
            if answer_dict.get('answer').upper() == 'Y':
                date = images_handler.get_date()

                response = {
                    'message': f'Origin date found: {date}.',
                    'status': 200
                }
            if answer_dict.get('answer').upper() == 'N':
                images_handler.increase_index()
                response = {
                    'message': 'Watch next image',
                    'status': 200
                }
            return response
        else:
            raise BadRequestError
    except BadRequestError:
        return {
            'message': 'The request must contain an "answer" key.',
            'status': 400
        }
    except Exception:
        print(traceback.format_exc())
        return {
            'message': 'There has been an error',
            'status': 500
        }
