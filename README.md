# 📝 Text Summarizer — HuggingFace T5

A text summarization web app built with a fine-tuned T5 transformer model, 
served via FastAPI with a custom dark-themed UI.

## 🔧 Tech Stack
- **Model**: T5 (fine-tuned) via HuggingFace Transformers
- **Backend**: FastAPI (Python)
- **Frontend**: Vanilla HTML/CSS/JS
- **Inference**: PyTorch (supports CUDA, MPS, CPU)

## 🚀 Run Locally
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Download the model (see below)
4. Run: `uvicorn app:app --reload`
5. Visit: `http://localhost:8000`

## 📦 Model
The fine-tuned model is hosted on HuggingFace Hub: [link here]
Download and place in `./saved_summary_model/`

## ✨ Features
- Real-time text summarization
- Cleans and preprocesses input automatically
- Beam search decoding for quality summaries
- Responsive, minimal dark UI