# Healthcare Management System Backend

This is a production-ready Django Backend for a Healthcare Management System. It uses Django REST Framework, PostgreSQL, and JWT for authentication.

## Prerequisites
- Python 3.10+
- PostgreSQL

## Setup Instructions

1. **Clone the repository or navigate to the project directory:**
   ```bash
   cd healthcare_backend
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   A `.env` file template is provided as `.env.example`.
   Rename it or use `.env` directly and ensure your PostgreSQL credentials are correct:
   ```env
   DB_NAME=healthcare_db
   DB_USER=postgres
   DB_PASSWORD=yourpassword
   DB_HOST=localhost
   DB_PORT=5432
   SECRET_KEY=django-insecure-replace-this-with-a-secure-key
   ```
   *Note: Ensure the PostgreSQL database `healthcare_db` actually exists on your local server.*

5. **Run Migrations:**
   ```bash
   python manage.py makemigrations authentication patients doctors mappings
   python manage.py migrate
   ```

6. **Create a Superuser (Optional, for admin panel access):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```
   The backend will start at `http://127.0.0.1:8000/`.

## API Documentation
A Postman collection `postman_collection.json` is provided in the root directory. You can import this directly into Postman to test all endpoints.

Make sure to replace the `{{access_token}}` variable in Postman with the actual token returned from the `/api/auth/login/` endpoint for authenticated requests.
