import uvicorn
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Interface de comunicação natudrive",
    version="1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"], 
)

if __name__ == '__main__':
    reload = True if os.getenv("ENV") == 'dev' else False
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=reload, workers=1)
