from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse 
from pydantic import BaseModel
from typing import List, Dict, Any
import json
# IMPORT NAME FIXED HERE:
from logic import IntegratedOrchestrator

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# INITIALIZATION FIXED HERE:
orch = IntegratedOrchestrator()

class ChatRequest(BaseModel):
    message: str
    history: List[Dict[str, str]]

@app.get("/")
async def read_index():
    """Serves the corporate dashboard at http://192.2.0.1:8000"""
    return FileResponse('index.html')

@app.post("/api/chat")
async def chat(request: ChatRequest):
    try:
        # User message enters, logic handles 10 MCP nodes in background
        response = orch.chat(request.message, request.history)
        return {"response": response}
    except Exception as e:
        # It's helpful to print(e) here during debugging to see Ollama/Network errors
        print(f"Error: {e}") 
        raise HTTPException(status_code=500, detail="An internal server error occurred.")

if __name__ == "__main__":
    import uvicorn
    # Listens on all interfaces so other machines can connect
    uvicorn.run(app, host="0.0.0.0", port=8000)