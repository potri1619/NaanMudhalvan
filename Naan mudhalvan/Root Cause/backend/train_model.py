import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load data
df = pd.read_csv('data/equipment_failures.csv')
X = df[['temperature', 'pressure', 'vibration', 'speed']]
y = df['label']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open('backend/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved.")
