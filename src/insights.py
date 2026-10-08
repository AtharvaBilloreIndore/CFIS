import pandas as pd

def summarize_clusters(df):
    summaries = []

    for cluster_id in df["cluster"].unique():
        cluster_data = df[df["cluster"] == cluster_id]

        summaries.append({
            "cluster": cluster_id,
            "count": len(cluster_data),
            "sentiment_distribution": cluster_data["sentiment"].value_counts().to_dict(),
            "sample_feedback": cluster_data["feedback"].head(2).tolist()
        })

    return pd.DataFrame(summaries)