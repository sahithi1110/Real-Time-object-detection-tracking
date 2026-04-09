import json
from confluent_kafka import Producer
from app.config import settings


class KafkaFrameProducer:
    def __init__(self):
        self.producer = Producer({
            "bootstrap.servers": settings.kafka_bootstrap_servers
        })

    def send(self, topic, payload):
        self.producer.produce(topic, json.dumps(payload).encode("utf-8"))
        self.producer.flush()