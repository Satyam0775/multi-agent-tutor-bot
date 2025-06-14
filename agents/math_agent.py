from tools.calculator import calculate

def handle_math_query(query: str) -> str:
    try:
        # Remove common non-math words
        expression = query.lower().replace("solve", "").replace("calculate", "").replace("what is", "").replace("=", "").strip()
        result = calculate(expression)
        return f"The answer is: {result}"
    except Exception as e:
        return f"Math error: {str(e)}"
