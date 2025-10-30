#!/bin/bash
# Railway startup script for UNI Connect

echo "🚀 Starting UNI Connect on port ${PORT:-8000}..."

# Use Railway's PORT or default to 8000
export PORT=${PORT:-8000}

# Start the FastAPI application
exec uvicorn app.main:app --host 0.0.0.0 --port $PORT --workers 1
