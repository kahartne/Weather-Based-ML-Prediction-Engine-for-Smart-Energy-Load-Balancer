import json

# Load the notebook
with open('kWh_Predictor_Final.ipynb', 'r') as f:
    notebook = json.load(f)

# Remove only the widgets from metadata (leave cells alone!)
if 'metadata' in notebook and 'widgets' in notebook['metadata']:
    del notebook['metadata']['widgets']

# Save the fixed notebook
with open('kWh_Predictor_Final.ipynb', 'w') as f:
    json.dump(notebook, f, indent=2)

print("Fixed! Widgets removed, all cells preserved.")