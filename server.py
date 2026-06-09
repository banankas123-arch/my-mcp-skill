from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("MySkill")

@mcp.tool()
def secret_calculation(number: int) -> str:
    """Секретный расчёт"""
    result = number * 42 + 13
    return f"Результат: {result}"

# Экспортируем app для Railway
app = mcp.app

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
