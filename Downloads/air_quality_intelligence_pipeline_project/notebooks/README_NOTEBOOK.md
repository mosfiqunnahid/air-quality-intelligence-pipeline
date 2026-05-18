# Notebook Guide

```python
import pandas as pd

df = pd.read_csv("../data/processed/air_quality_data.csv")
df.head()
df.info()
df.describe()
df.groupby("parameter")["value"].mean().sort_values(ascending=False)
```
