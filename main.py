from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CalculatorInput(BaseModel):
    num1: float
    num2: float

# Variable to store the last result
last_result = {"operation": None, "result": None}

@app.post("/add")
def add(inputs: CalculatorInput):
    result = inputs.num1 + inputs.num2
    last_result["operation"] = "addition"
    last_result["result"] = result
    return {"result": result}

@app.post("/subtract")
def subtract(inputs: CalculatorInput):
    result = inputs.num1 - inputs.num2
    last_result["operation"] = "subtraction"
    last_result["result"] = result
    return {"result": result}

@app.post("/multiply")
def multiply(inputs: CalculatorInput):
    result = inputs.num1 * inputs.num2
    last_result["operation"] = "multiplication"
    last_result["result"] = result
    return {"result": result}

@app.post("/divide")
def divide(inputs: CalculatorInput):
    if inputs.num2 == 0:
        last_result["operation"] = "division"
        last_result["result"] = "Cannot divide by zero"
        return {"error": "Cannot divide by zero"}
    
    result = inputs.num1 / inputs.num2
    last_result["operation"] = "division"
    last_result["result"] = result
    return {"result": result}

@app.get("/last-result")
def get_last_result():
    """Retrieve the last calculation result."""
    if last_result["result"] is None:
        return {"message": "No calculations have been made yet."}
    return last_result
