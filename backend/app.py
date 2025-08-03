import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse
from appUtils import *
import services.comic.routeDetails as comicsRoutes

app = FastAPI()

app.include_router(comicsRoutes.router)

origins = ["*"]

app.add_middleware(GZipMiddleware, minimum_size=512)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

log = putlog("MainExecutor")

configFile = "config/app.setting.json"
configuration = readJson(configFile)

@app.get("/")
def base():
    return JSONResponse({"Hello": "World"})


if __name__ == "__main__":
    uvicorn.run("app:app", 
                host=configuration["App"]["Host"],
                port=configuration["App"]["Port"], reload=True)
