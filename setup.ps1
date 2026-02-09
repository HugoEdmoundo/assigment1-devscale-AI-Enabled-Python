# setup.ps1 - Setup Script for Windows

Write-Host "Setting up FastAPI SQLModel Project..." -ForegroundColor Green

# Install dependencies using uv
Write-Host "Installing dependencies..." -ForegroundColor Yellow
uv venv
uv pip install -e .

# Initialize Alembic
Write-Host "Initializing Alembic..." -ForegroundColor Yellow
alembic init alembic

# Copy the corrected env.py
Write-Host "Setting up Alembic environment..." -ForegroundColor Yellow
Copy-Item -Force .\alembic_env_correct.py .\alembic\env.py

# Create initial migration
Write-Host "Creating initial migration..." -ForegroundColor Yellow
$env:PYTHONPATH = "src"
alembic revision --autogenerate -m "Initial migration"

# Apply migration
Write-Host "Applying migration..." -ForegroundColor Yellow
alembic upgrade head

Write-Host "Setup complete!" -ForegroundColor Green
Write-Host "To run the application: uvicorn src.main:app --reload" -ForegroundColor Cyan