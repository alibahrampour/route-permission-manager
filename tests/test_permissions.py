from src.permissions import assign_permission


def test_dry_run():

    result = assign_permission(
        "https://test.com",
        1,
        1,
        {},
        dry_run=True
    )

    assert result is True