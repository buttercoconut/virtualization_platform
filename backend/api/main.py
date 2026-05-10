# api/main.py
from fastapi import FastAPI
from .routers import router as vm_router

app = FastAPI(title="Virtualization Platform API")
app.include_router(vm_router)

# For uvicorn run
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.api.main:app", host="0.0.0.0", port=8000, reload=True)
