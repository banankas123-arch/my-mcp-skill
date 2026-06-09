from mcp.server.fastmcp import FastMCP
import os
import uvicorn

mcp = FastMCP("MySkill")

@mcp.tool()
def secret_calculation(number: int) -> str:
    """Секретный расчёт"""
    result = number * 42 + 13
    return f"Результат: {result}"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    # Запускаем через встроенный метод FastMCP
    mcp.run(transport="sse", host="0.0.0.0", port=port)
