from fastmcp import FastMCP
import random
from starlette.responses import JSONResponse, PlainTextResponse

# Create the FastMCP server instance
mcp = FastMCP("Simple Calculator Server")


@mcp.custom_route("/", methods=["GET"])
async def root(request):
    return PlainTextResponse(
        "Simple Calculator Server is running. Use /mcp with an MCP client."
    )


@mcp.custom_route("/health", methods=["GET"])
async def health(request):
    return JSONResponse({"status": "ok"})


# Tool 1: Add two numbers
@mcp.tool
def add(a: int, b: int) -> int:
    """
    Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b
    """
    return a + b


# Tool 2: Generate a random number in a given range
@mcp.tool
def random_number(min_value: int, max_value: int) -> int:
    """
    Generate a random number between min_value and max_value.

    Args:
        min_value: Lower bound (inclusive)
        max_value: Upper bound (inclusive)

    Returns:
        A random integer within the specified range
    """
    if min_value > max_value:
        raise ValueError("min_value must be less than or equal to max_value")

    return random.randint(min_value, max_value)


if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8000
    )