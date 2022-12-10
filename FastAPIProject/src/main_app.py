from fastapi import FastAPI
from src.utils.log_util import logger
import uvicorn
from src.apis.crud_app import router as crud_router


app = FastAPI()
# Routers
app.include_router(crud_router, prefix="/v1", tags=["CRUD APIs"])


@app.get('/')
def start():
    response = "Application running"
    return response


@app.get('/v1/health')
def health():
    logger.info("Request received for endpoint:/v1/health")
    response = "Application running"
    logger.info("Request completed for endpoint:/v1/health")
    return response


if __name__ == "__main__":
    uvicorn.run(app)

