import json
from confluent_kafka import Consumer
from app.config import settings


class KafkaFrameConsumer:
    def __init__(self, group_id="frame-consumer-group"):
        self.consumer = Consumer({
            "bootstrap.servers": settings.kafka_bootstrap_servers,
            "group.id": group_id,
            "auto.offset.reset": "earliest"
        })
        self.consumer.subscribe([settings.kafka_input_topic])

    def read_message(self):
        message = self.consumer.poll(1.0)
        if message is None:
            return None

        if message.error():
            return None

        return json.loads(message.value().decode("utf-8"))

    def close(self):
        self.consumer.close()