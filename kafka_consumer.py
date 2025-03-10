from kafka import KafkaConsumer
import json
import pymysql

# Connect to Kafka
consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

# Connect to SingleStore (MySQL)
conn = pymysql.connect(
    host='127.0.0.1',  
    user='root',
    password='SinglestoreDB',  
    database='transactions_db'
)

cursor = conn.cursor()

# Process incoming transactions
for message in consumer:
    transaction = message.value
    sql = "INSERT INTO transactions (account, amount, type, timestamp) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (transaction['account'], transaction['amount'], transaction['type'], transaction['timestamp']))
    conn.commit()
    print("✅ Stored transaction:", transaction)

conn.close()
