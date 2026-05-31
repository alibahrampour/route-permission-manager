from src.routes import get_routes


def test_module_exists():

    assert callable(
        get_routes
    )