from fastapi import FastAPI
from .api.routes import router
from .core.config import APP_NAME

app = FastAPI(title=APP_NAME, version="1.0.0")
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    from .core.config import HOST, PORT
    uvicorn.run("app.main:app", host=HOST, port=PORT, reload=True)
