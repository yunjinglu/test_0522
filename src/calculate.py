from fastapi import FastAPI
app = FastAPI()

def add_fun(a, b):
    return a + b


def sub_fun(a, b):
    # temp = 123
    return a - b


def mul_fun(a: float, b: float) -> float:
    # return 123
    return a * b

@app.get("/")
def home():
    return {"status": "Online", "message" : "這是簡易計算機API"}

@app.get("/add")
def add(a: float, b: float):
    result = add_fun(a, b)
    return {"operation" : "addition", "a": a, "b": b, "result": result}