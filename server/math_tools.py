from fastmcp import FastMCP

mcp = FastMCP("Math Server", instructions="A math utility server.")


def _add(a: float, b: float) -> float:
    """Add two numbers."""
    print(f"Adding {a} and {b}")
    return a + b


def _subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def _multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def _divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def _power(base: float, exponent: float) -> float:
    """Raise base to the power of exponent."""
    return base**exponent


def _sqrt(a: float) -> float:
    """Calculate the square root of a number."""
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return a**0.5


def _modulo(a: float, b: float) -> float:
    """Calculate a mod b."""
    if b == 0:
        raise ValueError("Cannot modulo by zero.")
    return a % b


def _factorial(n: int) -> int:
    """Calculate the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def _discriminant(a: float, b: float, c: float) -> float:
    """Calculate the discriminant (b^2 - 4ac) of the quadratic ax^2 + bx + c."""
    return b * b - 4 * a * c


def _solve_quadratic(a: float, b: float, c: float) -> dict:
    """Solve ax^2 + bx + c = 0 using the quadratic formula.

    Returns the discriminant, the number of real roots, and the roots.
    Complex roots are returned as strings like "-1.0+2.0i".
    """
    if a == 0:
        raise ValueError("Coefficient 'a' must be non-zero for a quadratic equation.")
    d = _discriminant(a, b, c)
    if d > 0:
        r = d**0.5
        roots = [(-b + r) / (2 * a), (-b - r) / (2 * a)]
        return {"discriminant": d, "real_roots": 2, "roots": roots}
    if d == 0:
        return {"discriminant": d, "real_roots": 1, "roots": [-b / (2 * a)]}
    re, im = -b / (2 * a), (-d) ** 0.5 / (2 * a)
    roots = [f"{re}+{abs(im)}i", f"{re}-{abs(im)}i"]
    return {"discriminant": d, "real_roots": 0, "roots": roots}


# MCP tools
mcp.tool()(_add)
mcp.tool()(_subtract)
mcp.tool()(_multiply)
mcp.tool()(_divide)
mcp.tool()(_power)
mcp.tool()(_sqrt)
mcp.tool()(_modulo)
mcp.tool()(_factorial)
mcp.tool()(_discriminant)
mcp.tool()(_solve_quadratic)

math_tools = [
    _add,
    _subtract,
    _multiply,
    _divide,
    _power,
    _sqrt,
    _modulo,
    _factorial,
    _discriminant,
    _solve_quadratic,
]
