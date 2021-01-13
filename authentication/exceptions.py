
from rest_framework.exceptions import ValidationError,_get_error_details



class AuthenticationError(ValidationError):

    def __init__(self, detail=None, code=None):
        detail= {
                    "non_field_errors": [
                    "Unable to log in with provided credentials."
                ],
                "status_code": 400
            }
        code = 400
        self.detail = _get_error_details(detail, code)

