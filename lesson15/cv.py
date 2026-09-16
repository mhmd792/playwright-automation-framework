import pandas as pd

df = pd.read_json("10 message task.jsonl", lines=True)
flat = pd.json_normalize(df.to_dict("records"))
flat.to_csv("phoenix_download.csv", index=False)