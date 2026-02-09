# run.ps1 - Run the application
$env:PYTHONPATH = "src"
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000