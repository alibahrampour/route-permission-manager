from src.retry import request_with_retry


def get_routes(base_url, headers):

    response = request_with_retry(
        "GET",
        f"{base_url}/api/routes/",
        headers=headers
    )

    return response.json()