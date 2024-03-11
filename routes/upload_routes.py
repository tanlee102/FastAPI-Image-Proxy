from fastapi import APIRouter, UploadFile, HTTPException
from PIL import Image
import io
import os
import requests

router = APIRouter()


@router.post("/img/v1/upload")
async def upload_image(image_path: UploadFile = None,
                       percent: int = 100,
                       pip_id: int = -1,
                       token: str = '_'
                       ):

    if image_path is None:
        return {"message": "No image provided."}

    # Read the uploaded image
    image = Image.open(image_path.file)

    # Resize the image
    resized_image = image.resize(
        (int(image.width * int(percent) / 100), int(image.height * int(percent) / 100))
    )

    # Create an in-memory file-like object
    resized_image_io = io.BytesIO()
    resized_image.save(resized_image_io, format="JPEG")
    resized_image_io.seek(0)

    # Prepare the handled image file to be sent as form data
    files = {"image": ("handled_image.jpg", resized_image_io, "image/jpeg")}

    # Send the handled image to a Node.js app URL using a POST request
    upload_url = os.getenv("PASS_UPLOAD_URL")
    url = f"{upload_url}?percent={str(percent)}&pip_id={str(pip_id)}&file_name={image_path.filename.split('.')[0]}"  # Replace with your Node.js app URL
    response = requests.post(url, files=files)

    if response.status_code == 200:
        return response.json()
    else:
        return {"message": "Error uploading image"}