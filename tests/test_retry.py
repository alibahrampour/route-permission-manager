from src.retry import request_with_retry


def test_retry_function_exists():

    assert callable(
        request_with_retry
    )