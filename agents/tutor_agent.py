from agents.math_agent import handle_math_query
from agents.physics_agent import handle_physics_query

def tutor_agent(question: str) -> str:
    if any(op in question for op in ['+', '-', '*', '/', '**']):
        return handle_math_query(question)
    elif any(const in question.lower() for const in ['speed of light', 'gravitational constant', 'planck constant', 'acceleration']):
        return handle_physics_query(question)
    else:
        return "Sorry, I can only help with math or physics questions."
