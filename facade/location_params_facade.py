from facade.facade_helper import validate_param_exists


class LocationParamsFacade:
    def __init__(self):
        self.coordinates = coordinates = {
            'longitude':
            {
                'max': 180.0,
                'min': -180.0
            },
            'latitude':
            {
                'max': 90,
                'min': -90
            }
        }

    def location_params_validation(self, dict):
        valid = self._validate_param_exists(dict, 'longitude')
        valid = valid and self._validate_coordinates(
            'longitude', dict.get('longitude'))
        valid = valid and self._validate_param_exists(dict, 'latitude')
        valid = valid and self._validate_coordinates(
            'latitude', dict.get('latitude'))
        valid = valid and self._validate_param_exists(dict, 'begin_date')
        valid = valid and self._validate_param_exists(dict, 'end_date')
        return valid

    def _validate_coordinates(self, coordinate, value):
        max = self.coordinates.get(coordinate).get('max')
        min = self.coordinates.get(coordinate).get('min')
        if value >= min and value <= max and type(value) == float:
            return True
        return False

    def _validate_param_exists(self, dict, param):
        return validate_param_exists(dict, param)


location_params_facade = LocationParamsFacade()
