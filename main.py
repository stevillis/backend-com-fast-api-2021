from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def hello(name: str):
    message = f'Hello {name}'
    return {"message": message}


@app.get('/square/{number}')
async def square(number: int):
    result = f'The equare of {number} is {number ** 2}'
    return {"result": result}
