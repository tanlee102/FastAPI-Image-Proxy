import httpx
import imghdr
from fastapi.exceptions import HTTPException
import io

async def fetch_image_data(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        image_data = response.content

    image_format = imghdr.what(None, h=image_data)
    if not image_format:
        raise HTTPException(status_code=400, detail="Invalid imageformat")

    return io.BytesIO(image_data)