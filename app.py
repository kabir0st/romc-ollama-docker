from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def hello(request: Request):
    return "Hello"
