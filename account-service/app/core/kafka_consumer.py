from kafka import KafkaConsumer
import json
from app.db.session import SessionLocal
from app.models.account import Account

consumer = KafkaConsumer(
    "transaction-topic",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

def consume_transactions():
    db = SessionLocal()

    for message in consumer:
        data = message.value

        sender = db.query(Account).filter(Account.id == data["from_account"]).first()
        receiver = db.query(Account).filter(Account.id == data["to_account"]).first()

        if sender and receiver:
            with db.begin():
                sender.balance -= data["amount"]
                receiver.balance += data["amount"]

           