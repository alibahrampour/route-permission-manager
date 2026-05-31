from src.retry import request_with_retry


def assign_permission(
        base_url,
        route_id,
        role_id,
        headers,
        dry_run=False):

    payload = {
        "route": route_id,
        "role": role_id
    }

    if dry_run:
        print(f"[DRY RUN] {payload}")
        return True

    response = request_with_retry(
        "POST",
        f"{base_url}/api/permissions/",
        headers=headers,
        json=payload
    )

    return response.status_code in [200, 201]