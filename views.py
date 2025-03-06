import asyncio
import logging

import httpx
from fastapi import HTTPException, APIRouter
from schemas import InputData


logger = logging.getLogger(__name__)


router = APIRouter()

@router.post("/process_data/")
async def process_data(input_data: InputData):
    """
    Эндпоинт для обработки входящих данных.
    Выполняет асинхронный запрос к внешнему API и возвращает объединённый результат.
    """
    # Асинхронный вызов внешнего API (получение случайного факта о кошках)
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            external_response = await client.get("https://catfact.ninja/fact")
            external_response.raise_for_status()
            cat_fact = external_response.json()
    except Exception as e:
        logger.error(f"Ошибка при вызове внешнего API: {e}")
        raise HTTPException(status_code=502, detail="Ошибка при вызове внешнего API")

    # Пример имитации асинхронной обработки (например, сложные вычисления)
    await asyncio.sleep(0.1)  # эмуляция задержки

    # Формирование итогового ответа
    result = {
        "received_data": input_data,
        "external_data": cat_fact
    }

    # Логирование результата обработки
    logger.info(f"Обработка завершена. Результат: {result}")

    # Опционально: сохранить данные в Redis (реализация зависит от выбранной библиотеки)

    return result