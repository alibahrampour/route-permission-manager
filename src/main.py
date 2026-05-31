import argparse

from config.settings import (
    BASE_URL,
    USERNAME,
    PASSWORD
)

from src.auth import get_token
from src.routes import get_routes
from src.permissions import assign_permission
from src.logger import setup_logger


logger = setup_logger()


def main():

    parser = argparse.ArgumentParser(
        description="Route Permission Manager"
    )

    parser.add_argument(
        "--role-id",
        required=True,
        help="Target role id"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without applying"
    )

    args = parser.parse_args()

    token = get_token(
        BASE_URL,
        USERNAME,
        PASSWORD
    )

    headers = {
        "Authorization": f"Bearer {token}"
    }

    routes = get_routes(
        BASE_URL,
        headers
    )

    logger.info(
        f"Found {len(routes)} routes"
    )

    success_count = 0

    for route in routes:

        result = assign_permission(
            BASE_URL,
            route["id"],
            args.role_id,
            headers,
            dry_run=args.dry_run
        )

        if result:
            success_count += 1

            logger.info(
                f"Permission assigned -> Route ID {route['id']}"
            )

    logger.info(
        f"Completed. Total assigned: {success_count}"
    )

    print(
        f"Finished. {success_count} routes processed."
    )


if __name__ == "__main__":
    main()