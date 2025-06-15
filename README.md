# multi-agent-tutor-bot
✅ Live Deployment Link
🌐 https://multi-agent-tutor-bot-git-main-satyam0775s-projects.vercel.app

✅ Final README Update
You can now update your README.md file like this:

# 🎓 Multi-Agent Tutor Bot

This is a simple FastAPI-based backend project that simulates a tutor bot with multiple agents (Math, Physics, General). It can handle different types of questions and respond using relevant logic for each subject.

## 🚀 Live Deployment

You can test the deployed project here:  
👉 [https://multi-agent-tutor-bot-git-main-satyam0775s-projects.vercel.app](https://multi-agent-tutor-bot-git-main-satyam0775s-projects.vercel.app)

## 🧠 Supported Endpoints

### `GET /`
Returns a welcome message.

### `POST /ask`
https://multi-agent-tutor-bot.vercel.app/ask
Send a question to the tutor bot.

#### Example (Using Postman or `curl`):
**POST Request Body (JSON):**
```json
{
  "question": "What is the gravitational constant?"
}
Response:

json

{
  "answer": "The value of gravitational constant is 6.674 × 10^-11 N·m²/kg²"
}
📁 Project Structure
bash
multi-agent-tutor-bot/
├── api/
│   └── main.py            # FastAPI app
├── agents/
│   ├── math_agent.py
│   ├── physics_agent.py
│   └── tutor_agent.py
├── tools/
│   ├── calculator.py
│   └── constants.py
├── .env
├── requirements.txt
├── README.md
├── .gitignore
├── vercel.json
🛠️ Tech Stack
FastAPI 🚀

Python 3.12 🐍

Vercel for deployment ☁️

Postman/cURL for testing 🔧

📄 License
MIT © 2025 Satyam Kumar
