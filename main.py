from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import example

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(example.router, prefix='/example')



