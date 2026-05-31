import requests


def get_token(base_url, username, password):

    response = requests.post(
        f"{base_url}/api/token/",
        json={
            "username": username,
            "password": password
        },
        timeout=30
    )

    response.raise_for_status()

    return response.json()["access"]