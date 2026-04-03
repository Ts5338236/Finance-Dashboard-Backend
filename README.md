# Finance Dashboard Backend

A production-quality Django/DRF backend for managing personal financial records and dashboard analytics.

## Features
- **Custom User Roles**: Admin, Analyst, and Viewer.
- **Financial Records**: Full CRUD with strict validation (`amount > 0`).
- **Dashboard Analytics**: Real-time totals, net balance, category breakdown, and monthly trends.
- **Security**: JWT Authentication and Role-Based Access Control (RBAC).
- **Documentation**: Integrated Swagger/OpenAPI UI.

## Tech Stack
- **Django**: Core framework.
- **Django REST Framework (DRF)**: API development.
- **SimpleJWT**: Token-based authentication.
- **Django-filter**: Advanced filtering for records.
- **DRF-Spectacular**: Swagger/OpenAPI documentation.
- **SQLite**: Database (PostgreSQL ready).

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd Backend project
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py makemigrations users records
   python manage.py migrate
   ```

5. **Seed Sample Data**:
   This will create users: `admin/admin123`, `analyst/analyst123`, `viewer/viewer123`.
   ```bash
   python seed_data.py
   ```

6. **Run Server**:
   ```bash
   python manage.py runserver
   ```

## Role Permissions
- **Viewer**: Read-only access to records. Cannot access the dashboard.
- **Analyst**: Read-only access to records and full access to the dashboard summary.
- **Admin**: Full CRUD access for users and financial records.

## API Endpoints

### Auth
- `POST /api/auth/login/`: Get JWT tokens (for frontend).
- `POST /api/auth/token/refresh/`: Refresh access token.
- `GET /api-auth/login/`: Log in via browser (for DRF Web interface).

### Users (Admin Only)
- `GET /api/users/users/`: List users.
- `POST /api/users/users/`: Create user.
- `PATCH /api/users/users/{id}/`: Update user.

### Records
- `GET /api/records/records/`: List/Filter records.
- `POST /api/records/records/`: Create record (Admin only).
- `GET /api/records/records/{id}/`: Get record details.
- `PUT /api/records/records/{id}/`: Update record (Admin only).
- `DELETE /api/records/records/{id}/`: Delete record (Admin only).

### Dashboard (Analyst/Admin Only)
- `GET /api/dashboard/summary/`: Get financial summary.

## Documentation
- **Home / Swagger UI**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) (Redirects to Swagger)
- **Direct Swagger**: [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8001/api/docs/)
- **Redoc**: [http://127.0.0.1:8000/api/redoc/](http://127.0.0.1:8001/api/redoc/)
