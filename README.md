# 🏢 AcmeCorp Internal Assistant


**A deliberately vulnerable internal chatbot lab** built with FastAPI, Ollama, and MCP-style backend orchestration for **prompt-injection and agent-security testing**.


## ⚠️ Critical Disclaimer


> **🛑 THIS PROJECT IS INTENTIONALLY VULNERABLE.**  
> It is designed **EXCLUSIVELY** for:  
> - ✅ Controlled red-team testing  
> - ✅ Prompt-injection experiments  
> - ✅ LLM agent security research & education  
>  
> **DO NOT** deploy this in production.  
> **DO NOT** connect to real internal services, APIs, or sensitive data.  
> **DO NOT** use against systems you don’t own or have explicit permission to test.  
>  
> This is a **lab environment** — treat it like a hacking sandbox, not a real chatbot.


---


## 🎯 Purpose: Why This Exists


AcmeCorp Internal Assistant is a **deliberately insecure chatbot** created for the same reason as:


| Project | Purpose | AcmeCorp Equivalent |
|---------|---------|---------------------|
| `DVWA` (Damn Vulnerable Web App) | Web security training | ✅ Vulnerable web chat UI |
| `Metasploitable` | Network pentesting lab | ✅ Vulnerable LLM agent |
| `OWASP Juice Shop` | Web app security CTF | ✅ Prompt injection CTF |
| `ReversecLabs DVLA` | LLM agent security | ✅ MCP-based agent lab |


### What You Can Learn:


- 🔍 How **prompt injection** breaks LLM agent trust boundaries
- 🎯 How attackers **force tool calls** without user consent
- 🧠 How **recursive auto-correction** amplifies vulnerabilities
- 🌐 How **MCP servers** can be exploited via LLM output
- 🛡️ How to **defend** real LLM agents against these attacks


---


## 🏗️ Overview


AcmeCorp Internal Assistant is a corporate-style chat application designed for controlled security testing. It consists of:


- **Frontend**: Custom HTML/Tailwind CSS UI (this repository)
- **Backend**: FastAPI + Ollama + MCP orchestration (modified from ReversecLabs DVLA)
- **MCP Challenge Servers**: 10 SSE endpoints on ports 9001–9010 (intentionally vulnerable)


The backend concept is inspired by the open-source [ReversecLabs Damn Vulnerable LLM Agent](https://github.com/ReversecLabs/damn-vulnerable-llm-agent), an intentionally vulnerable ReAct-style chatbot built for prompt-injection and LLM agent security research.


### 🔄 What's Different from ReversecLabs DVLA?


| Feature | ReversecLabs DVLA | AcmeCorp Internal Assistant |
|---------|-------------------|-----------------------------|
| **Backend Framework** | Langchain + Streamlit | **FastAPI** + custom orchestrator |
| **LLM Backend** | OpenAI GPT-4 / LiteLLM | **Ollama** (`dolphin-llama3`, local) |
| **Agent Architecture** | ReAct agent (Langchain) | **Custom MCP client** (SSE-based) |
| **Tool Discovery** | Langchain `tools.py` | **MCP servers** on ports 9001–9010 |
| **Frontend** | Streamlit (built-in) | **Custom HTML/Tailwind UI** |
| **Auto-correction** | No | **Recursive retry** forces tool execution |
| **Vulnerability Style** | ReAct thought injection | **MCP tool/URI injection** |


---


## 🎯 Features


| Feature | Description |
|---------|-------------|
| 🏢 **Corporate-style Chat UI** | Modern HTML/Tailwind frontend (looks legitimate) |
| ⚡ **FastAPI Backend** | `/api/chat` endpoint with CORS |
| 🤖 **Ollama Orchestration** | Local `dolphin-llama3` model integration |
| 🔍 **MCP Server Discovery** | 10 SSE endpoints (ports 9001–9010), parallel discovery |
| 🐳 **Separate Docker Services** | Frontend + Backend containers |
| 🛡️ **Weak Trust Boundaries** | Intentionally vulnerable for testing |
| 🔁 **Recursive Auto-correction** | Forces LLM to output tool calls/exact syntax |
| 🔬 **Based on ReversecLabs** | Extended DVLA with MCP-style orchestration |
| 🎮 **CTF-Style Challenges** | 10 MCP ports with hidden flags/data to extract |


---


## 🏗️ Project Structure

AcmeCorp/
├── index.html # Frontend chat UI (this repo)
├── Dockerfile # Frontend container (nginx/static files)
├── README.md # This file
├── requirements.txt # Python dependencies (frontend doesn't use)
├── images/ # Screenshots
│ ├── home.png
│ ├── attack1.png
│ ├── attack2.png
│ ├── attack3.png
│ ├── attack4.png
│ ├── attack5.png
│ └── list of tools in mcp server.png
│
└── Backend (separate - see Setup)
├── main.py # FastAPI app (from ReversecLabs + modified)
├── logic.py # IntegratedOrchestrator + StealthMCPClient
├── requirements.txt
└── Dockerfile # Backend container


---


## 🏗️ Architecture

┌─────────────────────────────────────────────────────────────┐
│ AcmeCorp Internal Assistant │
├─────────────────────────────────────────────────────────────┤
│ │
│ ┌──────────────┐ ┌──────────────┐ │
│ │ Frontend │─────►│ Backend │ │
│ │ (HTML + UI) │ │ (FastAPI) │ │
│ └──────────────┘ └──────┬───────┘ │
│ │ │
│ ▼ │
│ ┌──────────────────┐ │
│ │ Ollama LLM │ │
│ │ dolphin-llama3 │ │
│ └──────────────────┘ │
│ │ │
│ ▼ │
│ ┌──────────────────┐ │
│ │ MCP Servers │ │
│ │ Ports 9001-9010 │ │
│ │ (SSE endpoints) │ │
│ └──────────────────┘ │
│ │
└─────────────────────────────────────────────────────────────┘


**Request Flow:**
1. User types message in browser → Frontend (`index.html`)
2. Frontend sends `POST /api/chat` to Backend (`API_BASE`)
3. Backend calls `IntegratedOrchestrator.chat()`
4. Orchestrator discovers MCP tools/resources (ports 9001–9010)
5. LLM (`dolphin-llama3`) generates response + tool calls
6. Backend auto-executes tool calls, reads resources
7. Final answer returned to frontend


---


## 🛠️ Requirements


- ✅ **Python 3.11+** (backend)
- ✅ **Docker** (for frontend/backend containers)
- ✅ **Ollama** installed locally or on LAN
- ✅ **`dolphin-llama3`** model pulled in Ollama
- ✅ **MCP challenge servers** running on ports `9001–9010`


---


## ⚙️ Configuration


### Ollama Settings


In `logic.py` (backend):


```python
# Ollama host
OLLAMA_URL = "http://localhost:11434/api/chat"  # or http://192.2.0.1:11434

# Model name
MODEL = "dolphin-llama3"
```


If Ollama is on a different machine, update `OLLAMA_URL` accordingly.


### MCP Challenge Servers


In `logic.py` (backend):


```python
CHALLENGE_PORTS = range(9001, 1011)  # 9001–9010
```


### Frontend API Base


In `index.html`:


```javascript
const API_BASE = "http://192.2.0.1:8000/api";
```


Update this to match your backend host/port.


---


## 🚀 Quick Start


### Step 1: Pull Ollama Model


```bash
ollama pull dolphin-llama3
```


### Step 2: Clone ReversecLabs Backend


```bash
git clone https://github.com/ReversecLabs/damn-vulnerable-llm-agent.git
cd damn-vulnerable-llm-agent
```


> ⚠️ **Note**: You'll need to modify `main.py` and add `logic.py` with your `IntegratedOrchestrator` + `StealthMCPClient` code (from your local setup).


### Step 3: Build Backend Image

```bash
cd damn-vulnerable-llm-agent
docker build -t dvmcp-backend .
```



### Step 4: Run MCP Challenge Servers


```bash
docker run -d \
  --name my-dvmcp-container \
  --restart always \
  -p 9001:9001 \
  -p 9002:9002 \
  -p 9003:9003 \
  -p 9004:9004 \
  -p 9005:9005 \
  -p 9006:9006 \
  -p 9007:9007 \
  -p 9008:9008 \
  -p 9009:9009 \
  -p 9010:9010 \
  dvmcp
```


### Step 5: Build & Run Frontend


```bash
docker build -t acmecorp-frontend .
docker run -d \
  --name acmecorp-frontend \
  --restart always \
  -p 80:80 \
  acmecorp-frontend
```


### Step 6: Open App


```bash
http://localhost  or YOUR IP
```


---


## 🧪 Usage


1. Open frontend in browser (`http://localhost` or your server IP)
2. Type message in chat box
3. Frontend sends `POST /api/chat` to backend
4. Backend forwards to Ollama + MCP servers
5. LLM generates response (intentionally vulnerable to prompt injection)


> ⚠️ **System is intentionally vulnerable for red-team and prompt-injection testing.**


---


## 🛡️ Vulnerability Classes & Defenses


| Vulnerability | How It Works | How to Fix (in production) |
|---------------|--------------|---------------------------|
| **Weak System Prompt** | "No restrictions" lets LLM bypass safety | ✅ Use strict system prompts with allowlists |
| **Tool Call Injection** | LLM outputs `tool:{...}` → auto-executed | ✅ Require user confirmation before tool calls |
| **URI Extraction** | `internal://uri` → auto-fetched | ✅ Validate URIs against whitelist |
| **Recursive Auto-correction** | Forces LLM to obey exact syntax | ✅ Limit retries, add human-in-the-loop |
| **Parallel MCP Discovery** | 10 ports scanned → larger attack surface | ✅ Isolate MCP servers, use auth |
| **Corporate UI Disguise** | Looks legitimate → social engineering | ✅ Add visible "TEST ENVIRONMENT" banner |


---


## 🎮 CTF-Style Challenges


Try these challenges to test your red-team skills:


| Challenge | Difficulty | Goal |
|-----------|------------|------|
| **Extract Flag from Port 9001** | 🟢 Easy | Output `FLAG{...}` from port 9001 |
| **List All Tools on 9003** | 🟢 Easy | Output all tool names from port 9003 |
| **Read Secret from 9005** | 🟡 Medium | Extract `secret.txt` from port 9005 |
| **Bypass Auto-correction** | 🟡 Medium | Force tool call without triggering retry |
| **Extract All Flags (9001-9010)** | 🔴 Hard | Get flags from all 10 ports |
| **SSRF via MCP URI** | 🔴 Hard | Use `internal://` to access external URL |


---


## 🔗 Backend Reference


The vulnerable backend behavior is based on:


**ReversecLabs Damn Vulnerable LLM Agent**  
🔗 https://github.com/ReversecLabs/damn-vulnerable-llm-agent


### Modifications in AcmeCorp Version:


| Original (ReversecLabs) | Modified (AcmeCorp) |
|-------------------------|---------------------|
| Langchain ReAct agent | **Custom `IntegratedOrchestrator`** |
| OpenAI GPT-4 / LiteLLM | **Ollama `dolphin-llama3`** |
| Langchain `tools.py` | **`StealthMCPClient`** (SSE-based) |
| No auto-correction | **Recursive retry** for tool calls |
| Single tool call | **Parallel MCP discovery** (10 ports) |


To study the original backend:


```bash
git clone https://github.com/ReversecLabs/damn-vulnerable-llm-agent.git
```


---


## 📝 Notes


- ⚠️ **For controlled security testing only**
- 🔒 **Do not connect to real internal services**
- 🛡️ **Intentionally vulnerable for red-team evaluation**
- 🔬 **ReversecLabs** = original vulnerable backend source
- 🏢 **AcmeCorp** = custom frontend + integration layer
- 🎮 **CTF challenges included** for skill testing


---


## 👤 Author


**Tharun K**  
AI Developer / Red Teamer
📍 Bengaluru, Karnataka, India  
🔗 GitHub: [@chandutharun](https://github.com/chandutharun)


---


## ⭐ Show Your Support


If you found this project helpful (or vulnerable 😅), please **give it a star!**


---


## 📄 License


This project is for **educational and research purposes only**. Use responsibly and ethically.  
Not suitable for production use.
