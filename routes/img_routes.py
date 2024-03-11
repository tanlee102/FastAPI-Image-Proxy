from typing import Optional

from fastapi import APIRouter, HTTPException
# import logging
from starlette.responses import StreamingResponse
from utils import get_connection_from_pool
from cache import cache
from db import get_image_url
from db import get_image_url_nat
from image import fetch_image_data

router = APIRouter()

# Configure logging
# logging.basicConfig(level=logging.INFO)  # Set the logging level to ERROR or higher

# @router.get("/img/v1/{image_param}")
@router.get("/img/v1/{image_path:path}")
async def get_image(image_path: str):

    image_param = image_path[:-4] if image_path.endswith('.nat') or image_path.endswith('.vnt') else image_path

    if image_param in cache:
        image_data = cache[image_param]
    else:
        connection = get_connection_from_pool()
        if connection:
            if image_path.endswith('.nat'):
                url = get_image_url_nat(connection, image_param)
            else:
                url = get_image_url(connection, image_param)
            # url = get_image_url(connection, image_param)
            connection.close()  # Release the connection back to the pool

            try:
                image_data = await fetch_image_data(url)
                cache[image_param] = image_data
            except HTTPException as exc:
                raise exc
            except Exception as exc:
                raise HTTPException(status_code=400, detail="Error retrieving image")

    # Reset the position of the image_data to the beginning
    image_data.seek(0)

    headers = {
        "Cache-Control": "public, max-age=14400"  # Set cache control headers for 4 hour
    }

    return StreamingResponse(image_data, media_type="image/jpeg", headers=headers)