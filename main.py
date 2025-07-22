import argparse
from modules.trend_fetcher import fetch_trending_topics
from modules.image_captioning import extract_caption
from modules.embedding_generator import get_embeddings
from modules.vector_store import setup_vector_store, query_similar
from modules.rag_pipeline import generate_rag_response
from modules.trend_predictor import predict_trendability
import os

def main():
    parser = argparse.ArgumentParser(description="Social Media Trend Predictor")
    parser.add_argument("--input_text", type=str, help="Post caption text")
    parser.add_argument("--image_path", type=str, help="Path to image or gif", default=None)
    args = parser.parse_args()

    print("[1] Fetching current trends...")
    trends = fetch_trending_topics()

    print("[2] Processing user input...")
    content_text = args.input_text or ""
    if args.image_path:
        content_text += " " + extract_caption(args.image_path)

    print("[3] Generating embeddings and retrieving...")
    user_embedding = get_embeddings(content_text)
    vector_store = setup_vector_store(trends)
    similar_trends = query_similar(vector_store, user_embedding)

    print("[4] RAG-based analysis...")
    response = generate_rag_response(content_text, similar_trends)

    print("[5] Predicting trendability...")
    verdict = predict_trendability(content_text, similar_trends)

    print("\nFinal Verdict:", verdict)
    print("\nLLM Explanation:\n", response)

if __name__ == "__main__":
    main()