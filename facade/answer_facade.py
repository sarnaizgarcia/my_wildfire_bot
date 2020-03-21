from facade.facade_helper import validate_param_exists


class ValidateAnswer:
    def validate_answer(self, answer):
        valid = validate_param_exists(answer, 'answer')
        return valid


answer_validator = ValidateAnswer()
