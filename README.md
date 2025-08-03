# Basti Ki Pathshala Backend

This backend is a simple and efficient FastAPI application designed to manage user registrations for the Basti Ki Pathshala Foundation. It provides two core API endpoints for registering new volunteers/interns and for public access to the list of all registered users.

The project is built with:

FastAPI: The web framework for building the API.

SQLModel: An elegant library for data models and database interactions.

SQLite: A lightweight, file-based database for persistent data storage.

Uvicorn: A fast ASGI server to run the application.

## Setup

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn main:app --reload
```


Access API at: `http://localhost:8000`

## API Endpoints

### POST /register
Register new volunteer/intern:
```json
{
  "name": "Full Name",
  "email": "user@example.com",
  "role": "volunteer/intern"
}
```

### GET /users
List all registered users:
```json
[
  {
    "id": 1,
    "name": "Example User",
    "email": "user@example.com",
    "role": "volunteer",
    "registration_date": "2023-08-03T00:00:00"
  }
]
```

## Database
SQLite database (`database.db`) created automatically in project directory.
