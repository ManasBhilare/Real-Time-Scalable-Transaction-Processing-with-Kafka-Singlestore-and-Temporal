import joblib
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

data = pd.DataFrame({
    "amount": np.random.uniform(10, 1000, 1000),
    "account": np.random.choice(["user1", "user2", "user3"], 1000),
    "is_fraud": np.random.choice([0, 1], 1000, p=[0.95, 0.05])
})

X = data[['amount']]
y = data['is_fraud']
model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, 'fraud_model.pkl')

def detect_fraud(transaction):
    model = joblib.load('fraud_model.pkl')
    if model.predict([[transaction['amount']]])[0] == 1:
        print(f"⚠️ FRAUD DETECTED! Transaction: {transaction}")
