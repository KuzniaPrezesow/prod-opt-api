# prod-opt-api

A Python project for managing and optimizing production workflows with PostgreSQL database integration. This project includes CRUD operations for interacting with the database and a structured backend setup using SQLAlchemy.

---

## Features
- **CRUD Operations**: Create, Read, Update, and Delete functionality for database tables.
- **Database Integration**: Uses SQLAlchemy to interact with a PostgreSQL database.
- **Generated Models**: Auto-generated SQLAlchemy models from the database schema.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd prod-opt-api
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Generate `models.py`
The `models.py` file is not included in the repository and must be generated using `sqlacodegen`.

To generate it:

1. Ensure the `sqlacodegen` package is installed:
  ```bash
  pip install sqlacodegen
  ```
2. Run the following command to generate the models:
```bash
sqlacodegen postgresql://<username>:<password>@<host>:<port>/<database> > models.py
```
Example:
```bash
sqlacodegen postgresql://postgres:postgres@localhost:5433/wincon > models.py
```

## Usage
### Running the CRUD Script
To test CRUD operations on the database:

```bash
python crud.py
```
### Example CRUD Functions
Add a new user:
```python
create_user("John Doe", "john.doe@example.com")
```
Fetch all users:
```python
read_users()
```

## Notes
- The models.py file is dynamically generated and excluded from version control. Be sure to generate it before running the project.
- Ensure your PostgreSQL database is running and accessible using the connection details in DATABASE_URL.

## Future Improvements
- Integrate with Flask API for a complete backend solution.
- Add support for frontend frameworks like Svelte or Vue.
- Include automated testing for CRUD functionality.

## License
This project is licensed under a Proprietary License. All Rights Reserved. Unauthorized copying, modification, or distribution of this software is strictly prohibited.
