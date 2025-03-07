# FastAPI with Redis Caching

This is a FastAPI project that uses Redis for caching.

## Features
- FastAPI for building APIs
- Redis for caching data
- Docker support for easy setup

## Requirements
- Python 3.8+
- Redis
- Docker (optional, for containerized setup)

## Installation

### 1. Clone the repository
```sh
git clone https://github.com/ulisssey/fastapi-tz.git
cd fastapi-tz
```

## Using Docker

### 1. Build and run the container
```sh
docker-compose up --build
```

uvicorn main:app --host 0.0.0.0 --port 80 --reload

### 2. Stop the container
```sh
docker-compose down
```

## API Endpoints
| Method | Endpoint       | Description        |
|-------|---------------|--------------------|
| POST  | `/process_data/`      | Process given json |


