from fastapi import APIRouter
from src.utils.log_util import logger
from src.service.crud_service import read


router = APIRouter()


@router.get("")
def crud_read():
    logger.info("Request received for endpoint:/v1")
    response = read()
    logger.info("Request completed for endpoint:/v1")

    return response


