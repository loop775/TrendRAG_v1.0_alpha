import streamlit as st
from modules.trend_fetcher import fetch_trending_topics
from modules.image_captioning import extract_caption
from modules.embedding_generator import get_embeddings
from modules.vector_store import setup_vector_store, query_similar
from modules.rag_pipeline import generate_rag_response
from modules.trend_predictor import predict_trendability

st.set_page_config(page_title="Will it Trend?", layout="wide")
st.title("📈 Social Media Post Trendability Checker")

user_text = st.text_area("Enter your post caption")
user_image = st.file_uploader("Upload an image or gif (optional)", type=["png", "jpg", "jpeg", "gif"])

if st.button("Check Trendability"):
    with st.spinner("Fetching trends and analyzing..."):
        trends = fetch_trending_topics()
        caption = user_text

        if user_image is not None:
            with open("temp_upload.jpg", "wb") as f:
                f.write(user_image.read())
            caption += " " + extract_caption("temp_upload.jpg")

        embedding = get_embeddings(caption)
        vs = setup_vector_store(trends)
        similar = query_similar(vs, embedding)

        verdict = predict_trendability(caption, similar)
        explanation = generate_rag_response(caption, similar)

        st.success(verdict)
        st.markdown("### 📋 Explanation")
        st.write(explanation)

        st.markdown("### 🔥 Top Related Trends")
        for t in similar:
            st.write(f"- {t.page_content}")