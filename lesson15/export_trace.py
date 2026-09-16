import pandas as pd

try:
    from phoenix.client import Client
    df = Client().spans.get_spans_dataframe(project_identifier="phi3-homework")
except ImportError:
    import phoenix as px
    df = px.Client().get_spans_dataframe(project_name="phi3-homework")

df["latency_s"] = (pd.to_datetime(df["end_time"]) - pd.to_datetime(df["start_time"])).dt.total_seconds()

df.to_csv("traces_all.csv", index=False)
df[df["latency_s"] > 5].to_csv("traces_slow.csv", index=False)

print(f"Total spans: {len(df)} | Slow (>5s): {(df['latency_s'] > 5).sum()}")