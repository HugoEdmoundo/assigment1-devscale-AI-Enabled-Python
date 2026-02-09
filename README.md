# 🚀 FastAPI SQLModel SQLite Project

A modern **FastAPI** project built with **SQLModel**, **Alembic migrations**, and **SQLite**. This repository is submitted as **Assignment 1** for **Devscale AI-Enabled Python**. The project demonstrates clean architecture, type safety, validation, and production-ready API practices.

---

## 📋 Features

* ✅ **FastAPI** – High-performance modern web framework
* ✅ **SQLModel** – ORM combining SQLAlchemy & Pydantic
* ✅ **Alembic** – Database migrations
* ✅ **SQLite** – Lightweight relational database
* ✅ **Scalar** – Clean and modern API documentation
* ✅ **Modular Architecture** – Separation of concerns
* ✅ **Type Safety** – Full Python type hints
* ✅ **Validation** – Pydantic-based request validation
* ✅ **Dependency Injection** – FastAPI `Depends` pattern

---

## 🏗️ Project Structure

```
aienablade-assigment1/
├── src/                          # Application source code
│   ├── core/                     # Core utilities
│   │   └── db.py                 # Database engine & session
│   ├── models/                   # SQLModel definitions
│   │   └── item_model.py         # Item model
│   ├── router/                   # API routers
│   │   └── item_router.py        # Item endpoints
│   └── main.py                   # FastAPI entry point
├── alembic/                      # Alembic migrations
│   ├── versions/                 # Migration scripts
│   └── env.py                    # Alembic environment config
├── alembic.ini                   # Alembic configuration
├── pyproject.toml                # Dependencies & metadata
├── app.db                        # SQLite database (auto-generated)
├── README.md                     # Project documentation
├── setup.ps1                     # Windows setup script
└── start.ps1                     # Windows start script
```

---

## 🚀 Quick Start

### Prerequisites

* Python **3.13+**
* **uv** package manager
* **PowerShell** (Windows)

### Installation

Clone the repository and navigate to the project directory:

```powershell
cd C:\laragon\www\aienablade-assigment1
```

Create virtual environment and install dependencies:

```powershell
uv venv
uv pip install fastapi sqlmodel alembic scalar-fastapi uvicorn
```

### Database Setup

Set Python path and initialize Alembic:

```powershell
$env:PYTHONPATH = "src"
alembic init alembic
```

Replace `alembic/env.py` with the corrected configuration.

Generate and apply migrations:

```powershell
alembic revision --autogenerate -m "Create items table"
alembic upgrade head
```

### Run Application

```powershell
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

---

## 🌐 API Endpoints

| Method | Endpoint | Description     | Required Header |
| ------ | -------- | --------------- | --------------- |
| POST   | /items   | Create new item | X-App-Version   |
| GET    | /items   | Get items list  | None            |

### Create Item

```bash
curl -X POST "http://localhost:8000/items" \
  -H "Content-Type: application/json" \
  -H "X-App-Version: 1.0.0" \
  -d '{
    "name": "Laptop Gaming",
    "price": 15000000,
    "stock": 5
  }'
```

### Get Items

```bash
# All items
curl "http://localhost:8000/items"

# Search
curl "http://localhost:8000/items?search=laptop"

# Pagination
curl "http://localhost:8000/items?limit=10"
```

---

## 📊 Database Model

```python
class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(..., min_length=3)
    price: int = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    created_at: datetime = Field(default_factory=datetime.utcnow)
```

---

## 🔧 Development Commands

### Database Migrations

```powershell
alembic revision --autogenerate -m "Description"
alembic upgrade head
alembic downgrade -1
alembic current
```

### Run Server

```powershell
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
# or
.\start.ps1
```

---

## 📚 API Documentation

* **Scalar UI**: [http://localhost:8000/scalar](http://localhost:8000/scalar)
* **OpenAPI JSON**: [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)
* **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🧪 Validation Rules

* `name`: minimum 3 characters
* `price`: greater than 0
* `stock`: non-negative
* Header `X-App-Version`: required for POST
* Item name must be unique

**Error Responses**:

* `400` Bad Request – validation error
* `422` Unprocessable Entity – missing header/field
* `409` Conflict – duplicate item name

---

## 🐛 Troubleshooting

**ModuleNotFoundError: No module named 'src'**

```powershell
$env:PYTHONPATH = "src"
```

**Alembic not detecting models**

* Ensure all models are imported in `alembic/env.py`

**SQLite database locked**

* Stop running server
* Restart application

**Reset Database**

```powershell
Remove-Item app.db -ErrorAction SilentlyContinue
alembic upgrade head
```

---

## 🚀 Deployment Notes

* Remove `--reload`
* Use Uvicorn with workers
* Configure environment variables
* Add authentication & authorization

```env
DATABASE_URL=sqlite:///./app.db
API_VERSION=1.0.0
DEBUG=false
```

---

## 📄 License

MIT License

---

## 🙏 Acknowledgments

* FastAPI
* SQLModel
* Alembic
* Scalar

---

**Assignment:** Devscale AI-Enabled Python – Assignment 1

Happy Coding! 🎉
