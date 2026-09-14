# Todo App (FastAPI + Vue 3 + PostgreSQL)

Simple fullstack Todo application.

## Project structure

```
.
├── backend/                # FastAPI application
│   ├── app/
│   │   ├── __init__.py
│   │   ├── database.py     # SQLAlchemy engine/session setup
│   │   ├── main.py         # FastAPI app, CORS, routes
│   │   ├── models.py       # SQLAlchemy models
│   │   └── schemas.py      # Pydantic schemas
│   ├── Dockerfile
│   ├── .dockerignore
│   └── requirements.txt
├── frontend/                # Vue 3 (Vite) application
│   ├── src/
│   │   ├── components/
│   │   │   └── TodoList.vue
│   │   ├── App.vue
│   │   ├── config.js
│   │   └── main.js
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── nginx.conf
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── .env
│   └── .env.production
└── docker-compose.yml
```

## Running with Docker Compose

```bash
docker compose up --build
```

- Frontend: http://localhost:8080
- Backend API: http://localhost:8000/api/items
- PostgreSQL: localhost:5432 (user: `todo`, password: `todo`, db: `tododb`)

## Running locally without Docker

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Without a `DATABASE_URL` environment variable, the backend falls back to a local SQLite database (`local.db`).

To use PostgreSQL:

```bash
export DATABASE_URL="postgresql+psycopg2://todo:todo@localhost:5432/tododb"
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend reads the API base URL from `VITE_API_URL` (see `.env`).
