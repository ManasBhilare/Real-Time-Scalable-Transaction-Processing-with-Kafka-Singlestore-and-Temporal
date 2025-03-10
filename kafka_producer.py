from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

accounts = ["user1", "user2", "user3"]
transaction_types = ["debit", "credit", "transfer"]

while True:
    transaction = {
        "account": random.choice(accounts),
        "amount": round(random.uniform(10, 1000), 2),
        "type": random.choice(transaction_types),
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
    }
    producer.send("transactions", transaction)
    print("Sent transaction:", transaction)
    time.sleep(1)
