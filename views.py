import asyncio
import logging
import sys
import httpx
from fastapi import HTTPException, APIRouter
from schemas import InputData
from redis_client import store_request_response, get_request_response


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)


router = APIRouter()

@router.post("/process_data/")
async def process_data(input_data: InputData):
    """
    Processes incoming JSON, fetches an external API response, checks Redis cache,
    and stores/retrieves the result.
    """
    logger.info(f"process_data with input_data: {input_data}")
    request_id = input_data.data.get('cat')
    logger.info(f"key = {request_id} for input_data: {input_data}")
    cached_data = await get_request_response(request_id)
    if cached_data:
        return {"request_id": request_id, "result": cached_data}

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            logger.info(f"requesting get cat facts for key: {request_id}")
            external_response = await client.get("https://catfact.ninja/fact")
            external_response.raise_for_status()
            cat_fact = external_response.json()
    except Exception as e:
        logger.error(f"Occured error: {str(e)}")
        raise HTTPException(status_code=502, detail=f"Error fetching external API: {e}")

    await asyncio.sleep(2)

    result = {
        "received_data": input_data.data,
        "external_data": cat_fact
    }
    logger.info(f"Appended cat fact into input_data, cat_fact: {cat_fact}")

    await store_request_response(request_id, result)

    return {"request_id": request_id, "result": result}
