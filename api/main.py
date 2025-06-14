from fastapi import FastAPI, Request
from agents.tutor_agent import tutor_agent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Multi-Agent Tutor Bot 🎓"}

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    question = data.get("question", "")
    if not question:
        return {"answer": "Please provide a valid question."}
    
    response = tutor_agent(question)
    return {"answer": response}
