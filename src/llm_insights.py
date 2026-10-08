import ollama

def generate_insights(cluster_summary_df):
    prompt = "You are an AI product analyst.\n\n"
    prompt += "Here is customer feedback analysis:\n\n"

    for _, row in cluster_summary_df.iterrows():
        prompt += f"""
Cluster {row['cluster']}:
- Feedback count: {row['count']}
- Sentiment distribution: {row['sentiment_distribution']}
- Examples: {row['sample_feedback']}
"""

    prompt += """
Based on this:
1. Identify key customer pain points
2. Prioritize issues
3. Suggest actionable improvements
"""

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]
