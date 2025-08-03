from src.views.http_types.http_response import HttpResponse
from .errors_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .errors_types.http_bad_request import HttpBadRequestError
from .errors_types.http_not_found import HttpNotFoundError

def error_handler(error: Exception) -> HttpResponse:
    if isinstance(error, (
        HttpUnprocessableEntityError,
        HttpBadRequestError,
        HttpNotFoundError
    )):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server error",
                "detail": str(error)
            }]
        }
    )
