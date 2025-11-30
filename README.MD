# 🥟 HiMeal — 您吃了吗? (AI Voice Assistant)

**HiMeal** comes from the classic Chinese greeting **“您吃了吗？”**, meaning *“Have you eaten?”*.  
A friendly, caring question — and the core spirit of this assistant.

HiMeal is a voice-first conversational assistant focused on food, nutrition, and meal suggestions.  
Powered by a modular AI architecture:

- Streamlit frontend UI
- FastAPI + Haystack backend
- Extendable RAG knowledge base

---

## ✨ Features

- Natural discussion about meals & health
- Modular design for fast feature expansion
- Session-based conversation
- Future upgrades:
  - 🎤 Speech-to-text input (Whisper)
  - 🔊 TTS voice responses
  - ⚡ WebSocket streaming
  - 👤 Personalized diet preferences

---

## 📂 Project Structure

```
HiMeal_a-voice-assist/
│
├── frontend/              # Streamlit web UI
│   ├── app.py
│   └── requirements.txt
│
├── backend/               # FastAPI + Haystack logic
│   ├── main.py
│   ├── pipelines/
│   ├── models/
│   └── data/
│
├── LICENSE                # Apache License 2.0
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/<yourname>/HiMeal_a-voice-assist.git
cd HiMeal_a-voice-assist
```

### 2️⃣ Install Frontend

```bash
cd frontend
pip install -r requirements.txt
```

Create `.env` in `frontend/`:

```env
API_BASE=http://localhost:8000
```

### 3️⃣ Run Backend (placeholder for now)

```bash
cd backend
uvicorn main:app --reload --port 8000
```

### 4️⃣ Launch Frontend

```bash
cd frontend
streamlit run app.py
```

Visit 👉 http://localhost:8501

---

## 🗺️ Roadmap

| Feature | Status |
|--------|:-----:|
| Text-based chat | ✅ |
| FastAPI backend | 🚧 |
| Whisper STT voice input | 🔜 |
| TTS voice response | 🔜 |
| Streaming responses | 🔜 |
| Nutrition RAG knowledge base | 🔜 |
| Personal food preference profile | 🔜 |

---

## 🤝 Contributing

Issues and PRs are welcome —  
Let’s make HiMeal smarter and tastier together! 🍽️

---

## 📄 License

Apache License 2.0 © 2024 HiMeal Team
