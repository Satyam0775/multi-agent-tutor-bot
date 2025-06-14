from tools.constants import PHYSICS_CONSTANTS

def handle_physics_query(query: str) -> str:
    query_lower = query.lower()
    for constant, value in PHYSICS_CONSTANTS.items():
        if constant in query_lower:
            return f"The value of {constant} is {value}"
    return "Sorry, I couldn't find any matching physics constant."
