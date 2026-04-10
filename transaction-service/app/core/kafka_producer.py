from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def send_transaction_event(data):
    producer.send("transaction-topic", value=data)  # ✅ FIXED
    producer.flush()
    print("✅ Kafka message is sent")