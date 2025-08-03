from pydantic import BaseModel, constr, ValidationError, conint, EmailStr, condecimal
from src.views.http_types.http_request import HttpRequest
from src.main.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntityError

def create_customer_validator(http_request: HttpRequest) -> None:
    class BodyData(BaseModel):
        name: constr(min_length=1) # type: ignore
        age: conint(ge=18) # type: ignore
        phone: constr(min_length=11, max_length=20) # type: ignore
        email: EmailStr() # type: ignore
        category: constr(min_length=1) # type: ignore
        monthly_income: condecimal(ge=0) # type: ignore

    try:
        BodyData(**http_request.body)
    except ValidationError as err:
        raise HttpUnprocessableEntityError(err.errors()) from err
