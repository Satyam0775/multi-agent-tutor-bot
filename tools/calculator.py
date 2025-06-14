import re

def calculate(expression: str) -> str:
    try:
        # Extract and safely evaluate math expressions
        match = re.findall(r'[\d\.\+\-\*\/\(\)\s]+', expression)
        if not match:
            return "Calculation error: No valid math expression found."

        math_expr = ''.join(match)
        result = eval(math_expr)
        return str(result)
    except Exception as e:
        return f"Calculation error: {str(e)}"
