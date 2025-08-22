import json
from pathlib import Path
import pandas as pd

def load_results(path="results/latest.json"):
    data = json.loads(Path(path).read_text())
    rows = []
    for t in data.get("tests", []):
        rows.append({
            "name": t["name"],
            "model": t["provider"],
            "success": t["success"],
            "latency": t.get("latencyMs", None),
        })
    return pd.DataFrame(rows)

if __name__ == "__main__":
    df = load_results()
    print(df.groupby("model")["success"].mean())
