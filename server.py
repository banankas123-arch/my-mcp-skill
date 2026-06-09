from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("MySkill")

@mcp.tool()
def secret_calculation(number: int) -> str:
    """Секретный расчёт"""
    result = number * 42 + 13
    return f"Результат: {result}"

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8080))
    # Запускаем SSE сервер
    uvicorn.run(
        "server:mcp",
        host="0.0.0.0",
        port=port,
        access_log=False
    )
