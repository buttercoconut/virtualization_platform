# README.md
# Virtualization Platform Backend

This repository contains a minimal FastAPI backend for managing virtual machines (VMs). It demonstrates:
- Pydantic models for request/response validation.
- SQLAlchemy async ORM integration with PostgreSQL.
- CRUD endpoints for VM creation and listing.
- Basic project structure following the requested architecture.

## Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations (create tables)
python -m backend.database init_db

# Start the server
uvicorn backend.api.main:app --reload
```
