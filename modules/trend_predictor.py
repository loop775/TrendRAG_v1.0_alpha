def predict_trendability(post, trends):
    trend_keywords = [t.page_content.lower() for t in trends]
    matched = [word for word in trend_keywords if word in post.lower()]
    match_score = len(matched)

    if match_score >= 3:
        return "✅ High chance to trend"
    elif match_score == 2:
        return "🟡 Possibly trending, optimize with popular tags"
    else:
        return "🔴 Unlikely to trend, try aligning with current events"