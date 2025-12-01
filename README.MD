# 🥟 HiMeal — 您吃了吗? (AI Voice Assistant)

**HiMeal** comes from the classic Chinese greeting **“您吃了吗？”**, meaning *“Have you eaten?”*.  
A friendly, caring question — and the core spirit of this assistant.

HiMeal is a voice-first conversational assistant focused on everything you want to ask.  
Powered by a modular AI architecture:

- Streamlit frontend UI
- FastAPI + Haystack backend
- Extendable RAG knowledge base

---

## ✨ Features

- Natural discussion and daily advises
- Modular design for fast feature expansion
- Session-based conversation
- Future upgrades:
  - 🎤 Speech-to-text input (Whisper)
  - 🔊 TTS voice responses
  - ⚡ WebSocket streaming
  - 👤 Personalized context and know-your-habit

---

## 📂 Project Structure

```
HiMeal_a-voice-assist/
│
├── frontend/              # Streamlit web UI
│   └── app.py
│
├── backend/               # FastAPI + Haystack logic
│   ├── main.py
│   ├── pipelines/
│   ├── models/
│   └── data/
│
├── LICENSE                # Apache License 2.0
├── requirements.txt
├── .env
└── README.md
```

---

## 🚀 Quick Start


### 1️⃣ Clone the Repo

```bash
git clone https://github.com/wahahaha-hub/HiMeal_a-voice-assist.git
cd HiMeal_a-voice-assist
```

### 2️⃣ Install Packages
**recommended python version: 3.11**
```bash
pip install -r requirements.txt
```




### 3️⃣ Run Backend

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
| Text-based chat | 🚧 |
| FastAPI backend | 🚧 |
| Whisper STT voice input | 🔜 |
| TTS voice response | 🔜 |
| Streaming responses | 🔜 |
| RAG knowledge base | 🔜 |
| Personal context memory | 🔜 |

---

## 🤝 Contributing

Issues and PRs are welcome —  
Let’s make HiMeal smarter and more usable together! 🍽️

---

## 📄 License

Copyright 2025 wahahaha-hub

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

