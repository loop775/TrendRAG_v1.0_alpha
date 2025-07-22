# 🔥 Social Media Trendability Checker (RAG)

This project uses Retrieval-Augmented Generation (RAG) to assess whether a social media post (text or image) is likely to trend, based on current trending topics from platforms like Twitter and Google Trends.

## ✨ Features
- Accepts text, image, or gif as input
- Extracts image captions using BLIP
- Retrieves real-time trends using PyTrends or Twitter API
- Embeds user content and trends using OpenAI embeddings
- Uses FAISS for similarity search
- Performs RAG-based reasoning with LangChain
- Displays verdict and reasoning in CLI or Streamlit UI

## 🚀 Usage

### CLI
```bash
python main.py --input_text "your caption here" --image_path "path/to/image.jpg"
```

### Streamlit App
```bash
streamlit run streamlit_app.py
```

## 🧪 Example
Input: `"Is the new OnePlus 13 camera good?"` + image  
Output: `🟡 Possibly trending...`

## 🛠 Setup
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Create `.env` file with:
```
OPENAI_API_KEY=...
TWITTER_BEARER_TOKEN=...
```

## 📂 Project Structure
```
.
├── main.py
├── streamlit_app.py
├── .env.example
├── requirements.txt
├── modules/
│   ├── trend_fetcher.py
│   ├── image_captioning.py
│   ├── embedding_generator.py
│   ├── vector_store.py
│   ├── rag_pipeline.py
│   └── trend_predictor.py
```

## 🧾 License
MIT License
