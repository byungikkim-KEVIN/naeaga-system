# q0_test_main.py
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/echo")
async def echo(request: Request):
    try:
        data = await request.json()
        return {"you_sent": data["message"]}
    except Exception as e:
        return {"error": str(e)}
