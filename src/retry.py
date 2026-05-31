import time
import requests


def request_with_retry(
        method,
        url,
        retries=3,
        delay=2,
        **kwargs):

    last_error = None

    for attempt in range(retries):

        try:
            response = requests.request(
                method=method,
                url=url,
                timeout=30,
                **kwargs
            )

            response.raise_for_status()

            return response

        except requests.RequestException as error:

            last_error = error

            if attempt < retries - 1:
                time.sleep(delay)

    raise last_error