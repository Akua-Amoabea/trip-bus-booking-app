# TRIP - Bus Booking API

A RESTful bus booking backend built with **FastAPI** and **PostgreSQL**. The application provides user authentication, OTP email verification, bus and route management, seat selection, and booking functionality.

## Tech Stack

- **Python** - Backend programming language
- **FastAPI** - REST API framework
- **PostgreSQL** - Relational database
- **SQLAlchemy** - ORM and database operations
- **Alembic** - Database migrations
- **Redis** - Temporary OTP storage
- **JWT** - Authentication and authorization
- **SMTP** - Email verification
- **Docker Compose** - PostgreSQL and Redis services

## Features

- User registration and email OTP verification
- JWT-based authentication
- Access and refresh tokens
- Bus and route management
- Location management
- Seat management and selection
- Booking management
- Luggage management
- Redis-based temporary OTP storage
- PostgreSQL database integration
- Database schema migrations with Alembic

## Project Structure

```text
trip-bus-booking-app/
├── alembic/
│   └── versions/
├── app/
│   ├── config/
│   │   ├── config.py
│   │   └── database.py
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── main.py
│   └── requirement.txt
├── .env.example
├── .gitignore
├── alembic.ini
├── docker-compose.yml
└── README.md
```

## Prerequisites

Install the following:

- Python 3.12 or later
- Docker and Docker Compose
- Git

## Installation and Setup

### 1. Clone the repository

```bash
git clone git@github.com:Akua-Amoabea/trip-bus-booking-app.git
cd trip-bus-booking-app
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```
### 3. Install dependencies

```bash
pip install -r app/requirement.txt
```

### 4. Configure environment variables

Copy the example environment file:

```bash
cp .env.example .env
```

Update `.env` with your database credentials, SMTP credentials, secret key, and other required configuration values.

Never commit your actual `.env` file.

### 5. Start PostgreSQL and Redis

```bash
docker compose up -d
```

### 6. Run database migrations

```bash
alembic upgrade head
```

### 7. Start the FastAPI application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically generates interactive API documentation.

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

Use Swagger UI to explore and test the available endpoints.

## Environment Variables

The application uses environment variables for database connections, authentication, Redis, and email configuration.

See `.env.example` for the required configuration variables.

## Database Migrations

Create a new migration after modifying database models:

```bash
alembic revision --autogenerate -m "describe your changes"
```

Apply migrations:

```bash
alembic upgrade head
```

## Author

Akua Amoabea Nana Osafo
