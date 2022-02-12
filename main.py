from typing import Optional

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
    result = f'The square of {number} is {number ** 2}'
    return {"result": result}


@app.get('/double')
async def double(number: int):
    result = f'The double of {number} is {number * 2}'
    return {"result": result}


@app.get('/rectangle-area')
async def rect_area(width: int, height: int):
    area = width * height
    return {"result": f"The area of a rectangle with {width}m width and {height}m height is {area}m²"}


@app.get('/double-and-square')
async def double_and_square(dbl: Optional[int] = None,
                            sqr: Optional[int] = None):
    final_result = []
    if dbl is not None:
        double_result = f'The double of {dbl} is {dbl * 2}'
        final_result.append(double_result)

    if sqr is not None:
        square_result = f'The square of {sqr} is {sqr ** 2}'
        final_result.append(square_result)

    return {"result": final_result}
