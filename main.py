from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
from os import system

# from core.settings import STATIC_DIR, STATIC_URL
from endpoints import router

app = FastAPI()

# app.mount(STATIC_URL, StaticFiles(directory=STATIC_DIR), name="static")
app.include_router(router)


if __name__ == '__main__':
    system("uvicorn main:app --reload")
