from src.schemas.http_request import HttpRequest
from src.schemas.http_response import HttpResponse
from src.use_cases.factories.make_create_product_use_case import make_sqlite_get_product_use_case


def create(request: HttpRequest) -> HttpResponse:
    """."""
    # TODO: colocar validador

    create_product_use_case = make_sqlite_get_product_use_case()

    create_product_use_case.execute(request.body)

    return HttpResponse(
        status_code=201,
        body={
            "message": "Product created.",
        },
    )
