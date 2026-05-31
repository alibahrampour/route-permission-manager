# Route Permission Manager

Bulk Route Permission Assignment Tool for Role-Based Access Control (RBAC) systems.

This tool automatically retrieves all available routes from a target application and assigns them to a specified role. It is designed for administrators, QA engineers, and developers who need to manage permissions across large numbers of routes.

---

## Features

* Assign permissions to all routes automatically
* Custom Role ID support
* Dry Run mode (preview changes without applying)
* Retry mechanism for unstable API calls
* Logging support
* Environment variable configuration
* Unit tests with pytest
* Cross-platform (Windows/Linux)

---

## Use Cases

* Initial RBAC setup
* Permission migration
* Test environment preparation
* Bulk permission assignment
* QA automation environments

---

## Installation

Clone the repository:

```bash
git clone https://github.com/alibahrampour/route-permission-manager.git

cd route-permission-manager
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file based on the example:

```bash
cp examples/.env.example .env
```

Example:

```env
BASE_URL=https://example.com

USERNAME=admin

PASSWORD=secret

ROLE_ID=1

RETRY_COUNT=3
```

---

## Usage

Assign permissions to a specific role:

```bash
python src/main.py --role-id 5
```

---

## Dry Run

Preview changes without sending requests:

```bash
python src/main.py --role-id 5 --dry-run
```

Example:

```text
[DRY RUN] {'route': 101, 'role': 5}
[DRY RUN] {'route': 102, 'role': 5}
[DRY RUN] {'route': 103, 'role': 5}
```

---

## Logging

Execution logs are automatically saved to:

```text
logs/execution.log
```

Example:

```text
2025-08-01 15:00:00 | INFO | Found 245 routes
2025-08-01 15:00:01 | INFO | Permission assigned -> Route ID 101
2025-08-01 15:00:02 | INFO | Permission assigned -> Route ID 102
```

---

## Project Structure

```text
route-permission-manager/

├── src/
├── config/
├── tests/
├── examples/
├── logs/
├── README.md
├── requirements.txt
└── setup.py
```

---

## Running Tests

```bash
pytest
```

---

## Roadmap

* [x] Bulk permission assignment
* [x] Dry Run mode
* [x] Retry mechanism
* [x] Logging support
* [x] Unit tests
* [ ] CSV export
* [ ] GitHub Actions CI/CD
* [ ] Docker support
* [ ] Multi-role assignment

---

## Contributing

Pull requests are welcome.

For major changes, please open an issue first to discuss what you would like to change.

---

## License

MIT License

```
```
