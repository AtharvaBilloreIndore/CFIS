import pandas as pd

from preprocess import clean_text
from sentiment import get_sentiment
from categorize import categorize_feedback
from embeddings import generate_embeddings
from clustering import cluster_feedback
from insights import summarize_clusters
from llm_insights import generate_insights


# Load data
df = pd.read_csv("data/feedback.csv")

# Phase 1–2 pipeline
df["cleaned_feedback"] = df["feedback"].apply(clean_text)
df["sentiment"] = df["feedback"].apply(get_sentiment)
df["category"] = df["feedback"].apply(categorize_feedback)

embeddings = generate_embeddings(df["cleaned_feedback"].tolist())
clusters = cluster_feedback(embeddings, n_clusters=3)
df["cluster"] = clusters

print("\nFeedback with clusters:\n")
print(df[["feedback", "sentiment", "cluster"]])

# Phase 2 summary
summary_df = summarize_clusters(df)

print("\nCluster Insights (Structured):\n")
print(summary_df)

# Phase 3 — LLM reasoning
llm_output = generate_insights(summary_df)

print("\nLLM GENERATED INSIGHTS:\n")
print(llm_output)
