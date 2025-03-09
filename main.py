import logging

from fastapi import FastAPI
import uvicorn

from config import sentiment_pipeline
app = FastAPI()
logger = logging.getLogger(__name__)

@app.get('/')
async def root() -> dict[str, str]:
    return {
        'response': 'The service is live'
    }


@app.post('/prediction')
async def prediction(text: str) -> dict[str, dict | str]:
    try:
        result = sentiment_pipeline(text)[0]

    except Exception as e:
        logger.exception(f'Exception: {e}')
        result = 'Unfortunatelly, something went wrong.'

    return {
        'response': result
    }


if __name__ == '__main__':
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=8000
    )
