# Route Permission Manager

A Python utility for synchronizing route-based permissions and assigning them to a target role through REST APIs.

## Features

* OAuth token authentication
* Route discovery via API
* Bulk permission assignment
* Batch processing
* Dry-run mode
* Configurable endpoints
* Environment variable support

## Installation

```bash
git clone https://github.com/yourusername/route-permission-manager.git

cd route-permission-manager

pip install -r requirements.txt
```

## Configuration

Create a .env file:

```env
CLIENT_ID=your-client-id
REFRESH_TOKEN=your-refresh-token
ROLE_ID=123

AUTH_URL=https://example.com/oauth/token
ROUTES_URL=https://example.com/api/routes
ASSIGN_URL=https://example.com/api/roles/actions/add
```

## Usage

Run permission synchronization:

```bash
python src/main.py
```

Preview changes without applying:

```bash
python src/main.py --dry-run
```

Custom batch size:

```bash
python src/main.py --batch-size 100
```

## Use Cases

* RBAC administration
* Permission migration
* Environment synchronization
* API-driven access management

## Tech Stack

* Python
* Requests
* REST APIs
* OAuth2
* RBAC

## License

MIT
