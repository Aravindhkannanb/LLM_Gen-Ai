# Research Paper Query Assistant

## Overview

A sophisticated Flask-based AI application that leverages advanced semantic search and language models to retrieve and generate insights from research papers.

## 🚀 Features

- Semantic search across research paper collections
- AI-powered contextual response generation
- User-friendly web interface
- Retrieval-augmented generation using state-of-the-art models

## 📋 Prerequisites

- Python 3.8+
- pip
- Virtual environment (recommended)

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/research-paper-query-assistant.git
cd research-paper-query-assistant
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 📦 Dependencies

- Flask
- Transformers
- Sentence-Transformers
- NumPy
- Faiss
- Torch

## 🛠 Configuration

### Required Files

Before running the application, ensure you have:

1. `faiss_index.index`: FAISS index for semantic search
2. `metadata.json`: Metadata for research papers
3. Trained models downloaded

### Model Configuration

- Embedding Model: `all-MiniLM-L6-v2`
- Language Model: `meta-llama/Llama-3.2-1B`

## 🖥 Running the Application

```bash
python app.py
```

Access the application at `http://localhost:5000`

## 🔍 How It Works

1. User enters a research query
2. Application performs semantic search across paper index
3. Retrieves top relevant papers
4. Generates AI-powered contextual response

## 🚧 Limitations

- Response quality depends on underlying AI models
- Performance tied to paper index size
- Computational resource constraints

## 📂 Project Structure

```
research-paper-query-assistant/
│
├── app.py               # Main Flask application
├── requirements.txt     # Project dependencies
├── faiss_index.index    # Semantic search index
├── metadata.json        # Paper metadata
│
└── templates/
    ├── index.html       # Search interface
    └── response.html    # Results page
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some feature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
