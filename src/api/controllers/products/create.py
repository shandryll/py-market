from schemas.http_request import HttpRequest
from schemas.http_response import HttpResponse
from use_cases.factories.sqlite.make_create_product_use_case import make_create_product_use_case


def create_product(request: HttpRequest) -> HttpResponse:
    """."""
    # TODO: colocar validador

    create_product_use_case = make_create_product_use_case()

    create_product_use_case.execute(request.body)

    return HttpResponse(
        status_code=201,
        body={
            "message": "Product created.",
        },
    )
