# Outfit Recommender

A machine learning fashion model packaged as an API that can offers recommendations for combinations of outfits to wear

## 🚀 Quickstart

### 1. Prerequisites

- Python 3.12+
- Git

### 2. Clone & Setup

```bash
git clone https://github.com/Incognitol07/outfit-recommender.git
cd outfit-recommender

cp .env.example .env

# Python venv
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# Install Python deps
pip install --upgrade pip
pip install -r requirements.txt

```

### 4. Running Locally

```bash
uvicorn app.main:app --reload
```

- Open <http://127.0.0.1:8000/docs> for Swagger UI.  
