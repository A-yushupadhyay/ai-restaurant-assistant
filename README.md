# 🍽️ AI Restaurant Assistant

An **AI-powered restaurant chatbot** that behaves like a **real human waiter** — guiding users step by step, understanding changing preferences, and recommending dishes intelligently.

This project is built as a **production-grade full-stack system**, focusing on **correctness, UX, cloud integration, and testability** rather than hype.

---

## 🚀 Live Demo

- **Frontend (Vercel)**: https://ai-restaurant-assistant.vercel.app  
- **Backend (Render)**: https://ai-restaurant-assistant-hs0j.onrender.com

<img width="1920" height="1080" alt="Screenshot (319)" src="https://github.com/user-attachments/assets/03cf9a57-0bc2-4fde-8c3e-5dbe490fc937" />

<img width="1920" height="1080" alt="Screenshot (318)" src="https://github.com/user-attachments/assets/311cdfac-00b3-43c8-ae9e-81b8445214f3" />


<img width="1920" height="1080" alt="Screenshot (315)" src="https://github.com/user-attachments/assets/97fa5911-8a9f-4a54-bd73-9a3c52d4761d" />

 
---


## 🎯 Why This Project?

Most AI chatbots:
- recommend too early  
- forget user context  
- break when users change their mind  

This project solves those problems by combining:
- **Human-like conversation pacing**
- **Decision-tree + AI hybrid UX**
- **Session-aware preference tracking**
- **Diff-aware recommendations**

👉 The result feels like talking to a **real restaurant waiter**, not a search engine.

---

## 🧠 Key Features

### 💬 Human Waiter Conversation Flow
- Natural greeting
- One question at a time (diet → taste → budget)
- Avoids overwhelming the user
- Handles mid-conversation changes

```Example**

User: Hi
Bot: Welcome 😊 Are you looking for vegetarian or non-veg today?

User: Vegetarian
Bot: Nice choice 👍 Any spice preference or budget?

User: Actually make it non-veg
Bot: Got it 👍 Updating your preferences…
```


---

### 🔁 Context-Aware Preference Updates
- Users can change preferences anytime:
  - “Actually make it non-veg”
  - “Under ₹250”
- Old recommendations disappear automatically
- Only relevant dishes are shown

---

### 🧩 QuickAction Buttons (Customer-Care UX)
- Button + chat hybrid interface
- Reduces typing friction
- Matches real customer-support chat flows
- Frontend-only → zero backend risk

---

### 🍽️ Smart Recommendation Engine
- Deterministic filtering (no hallucinations)
- Filters by:
  - Diet (veg / non-veg)
  - Taste (spicy / mild)
  - Budget
  - Health flags
- AI is used only to **explain**, not to decide

---

### 🖼️ Menu Upload System
- Upload menu as:
  - ✅ JSON
  - ✅ PDF
  - ✅ Image
- Files stored securely in **AWS S3**
- Backend remains stateless
- OCR-ready architecture

---

### ☁️ AWS S3 Integration
- Secure file storage
- IAM-based access
- No public bucket exposure
- Production-ready cloud design

---

### 🧪 Automated Testing (Pytest)
- Conversation logic tests
- Menu filtering tests
- Prevents regressions
- Demonstrates real-world testing discipline

---

## 🛠️ Tech Stack

### Frontend
- React
- Tailwind CSS
- Vercel (deployment)

### Backend
- FastAPI
- Python 3.12
- Uvicorn
- Render (deployment)

### AI
- OpenAI (intent extraction + response generation)

### Cloud
- AWS S3
- IAM

### Testing
- Pytest

---

# 🏗️ Architecture Overview

```bash 

┌─────────────────────┐
│   Frontend (React)  │
│  • Chat UI          │
│  • QuickActions     │
│  • Menu Upload      │
└─────────┬───────────┘
          │ HTTP
          ▼
┌─────────────────────┐
│  FastAPI Backend    │
│  • API Routing      │
│  • Session Handling │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Intent Extraction   │
│ (OpenAI)            │
│ • Understand user   │
│ • No decisions      │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Conversation State  │
│ • Session store     │
│ • Context memory    │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Menu Engine         │
│ • Deterministic     │
│ • Filter rules      │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ AI Response Layer   │
│ • Explain choices   │
│ • Human tone        │
└─────────────────────┘



**Design principle**
- AI understands
- Code decides
- AI explains

This prevents hallucinations and ensures correctness.
```

---

## 🧪 Run Locally

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```
```Frontend
cd frontend
npm install
npm run dev
```
```🧪 Run Tests
cd backend
pytest
```
### 🧠 Key Design Decisions (Interview Ready)
- Why decision-tree + AI hybrid?
Pure AI is unreliable for business rules

- Deterministic logic ensures correctness

- AI improves tone and flexibility

- Why session-based memory?
Real conversations require memory

- Enables “change your mind” behavior

- Easily replaceable with Redis later

- Why AWS S3?
Stateless backend

- Scalable file storage

- Industry-standard cloud solution

### 📈 What This Project Demonstrates
- Full-stack engineering

- Real-world UX design

- Cloud integration (AWS)

- API design

State management

- Automated testing

- Production deployment


### 🚀 Future Improvements
- OCR parsing via AWS Lambda

- Redis-backed session store

- Multi-restaurant support

- Analytics dashboard

- Image-based dish cards

### 👨‍💻 Author
Ayush Upadhyay <br>
Aspiring Software Engineer (SDE) <br>
Focused on building production-grade systems
