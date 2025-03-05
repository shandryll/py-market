from schemas.http_request import HttpRequest
from schemas.http_response import HttpResponse
from use_cases.factories.sqlite.make_create_product_use_case import make_create_product_use_case


def create_product(request: HttpRequest) -> HttpResponse:
    """."""
    # TODO: colocar validador

    create_product_use_case = make_create_product_use_case()

    response = create_product_use_case.execute(request)

    return HttpResponse(
        body=response.body,
        status_code=response.status_code,
    )
