import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello() -> dict:
    return {"msg": "Hello World"}


@app.get("/echo/{msg}")
async def echo(msg: str) -> dict:
    return {"msg": f"{msg}"}


@app.post("/callback")
async def callback() -> dict:
    return {"callback": "Hello World"}


@app.get("/healthcheck")
async def healthcheck() -> dict:
    return {"healthcheck": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)