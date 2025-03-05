from schemas.http_request import HttpRequest
from schemas.http_response import HttpResponse
from use_cases.factories.sqlite.make_get_product_use_case import make_get_product_use_case


def get_product(request: HttpRequest) -> HttpResponse:
    """."""
    # TODO: colocar validador

    get_product_use_case = make_get_product_use_case()

    response = get_product_use_case.execute(request.params["name"])

    return response
