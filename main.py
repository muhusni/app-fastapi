from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import router as api_router

app = FastAPI()

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")
# Include the routes
app.include_router(api_router)
