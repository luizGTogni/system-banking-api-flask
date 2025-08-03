from pydantic import BaseModel, ValidationError, condecimal
from src.views.http_types.http_request import HttpRequest
from src.main.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntityError

def withdraw_customer_validator(http_request: HttpRequest) -> None:
    class BodyData(BaseModel):
        value: condecimal(gt=0) # type: ignore

    try:
        BodyData(**http_request.body)
    except ValidationError as err:
        raise HttpUnprocessableEntityError(err.errors()) from err
