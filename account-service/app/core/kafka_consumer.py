from kafka import KafkaConsumer
import json
from app.db.session import SessionLocal
from app.models.account import Account
from fastapi import Depends,HTTPException
from kafka import KafkaConsumer
import time

def get_kafka_consumer():
    while True:
        try:
            consumer = KafkaConsumer(
                "transaction-topic",
                bootstrap_servers="kafka:9092",
                group_id="transaction-group-v2",
                auto_offset_reset="earliest",
                value_deserializer=lambda m: json.loads(m.decode("utf-8")),
            )
            print("Kafka connected ✅", flush=True)
            return consumer

        except Exception as e:
            print(f"❌ Kafka not ready, retrying... {e}", flush=True)
            time.sleep(5)
    
  


def consume_transactions():
    print("🔥 Consumer started", flush=True)

    consumer = get_kafka_consumer()   # ✅ ONLY ONCE
    print("received consumer")
    while True:
        print("waiting for message")
        try:
            for message in consumer:
                handle_message(message)

        except Exception as e:
            print("🚨 Consumer crashed:", e, flush=True)
            time.sleep(5)

def handle_message(message):
    try:
        data = message.value
        print("📩 Received:", data)

        amount = data.get("amount")
        if amount is None:
            print("❌ Missing amount:", data)
            return

        from_account_id = data.get("from_account")
        to_account_id = data.get("to_account")
        if not from_account_id or not to_account_id:
            print("❌ Missing account IDs:", data)
            return

        db = SessionLocal()
        try:
            sender = db.query(Account).filter(Account.id == from_account_id).first()
            receiver = db.query(Account).filter(Account.id == to_account_id).first()

            if sender and receiver:
                if sender.balance >= amount:
                    sender.balance -= amount
                    receiver.balance += amount
                    db.commit()
                    print("💰 Transaction success")
                else:
                    print("❌ Insufficient balance")
            else:
                print("❌ Account not found")

        except Exception as e:
            print("❌ Error processing:", e)
            db.rollback()
        finally:
            db.close()

    except Exception as e:
        print("❌ Error processing message:", e)