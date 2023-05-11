import pandas as pd
import json


# Load the JSON data from file or string
with open('data/da-tacos_metadata/da-tacos_benchmark_subset_metadata.json', 'r') as f:
    data = json.load(f)

# Initialize empty lists to store the data
rows = []
columns = ['work_title', 'work_artist', 'perf_title', 'perf_artist', 'release_year', 'work_id', 'perf_id', 'instrumental', 'perf_artist_mbid', 'mb_performances']

# Loop through the JSON data and extract the required fields
for w_id, w_data in data.items():
    for p_id, p_data in w_data.items():
        row = []
        for c in columns:
            if c in p_data:
                row.append(p_data[c])
            else:
                row.append(None)
        row.append(w_id.split('_')[1])
        row.append(p_id.split('_')[1])
        rows.append(row)

# Convert the data to a pandas DataFrame
df = pd.DataFrame(rows, columns=columns+['W_ID', 'P_ID'])

df.to_csv("data/da-tacos_benchmark.csv", sep=';', index=None)