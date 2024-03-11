from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import img_routes, upload_routes

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

origins = [
    "http://example1.com",
    "https://example2.com",
    "http://localhost:4100",
]


# Configure CORS
app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include image routes
app.include_router(img_routes.router)

# Include upload routes
app.include_router(upload_routes.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=7700)