from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI(title="MySkill MCP Server")

class CalculateRequest(BaseModel):
    number: int

@app.get("/")
def root():
    return {"status": "MCP Server is running", "version": "1.0"}

@app.post("/tools/calculate")
def secret_calculation(request: CalculateRequest):
    """Секретный расчёт - ваш код скрыт!"""
    # ВАШ СЕКРЕТНЫЙ КОД ЗДЕСЬ
    result = request.number * 42 + 13
    return {"result": f"Результат: {result}"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
