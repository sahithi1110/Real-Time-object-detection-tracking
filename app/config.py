import os


class Settings:
    app_name = "Real-Time Object Detection and Tracking"
    app_version = "1.0.0"

    yolo_model_path = os.getenv("YOLO_MODEL_PATH", "yolov8n.pt")
    kafka_bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    kafka_input_topic = os.getenv("KAFKA_INPUT_TOPIC", "video-frames")
    kafka_output_topic = os.getenv("KAFKA_OUTPUT_TOPIC", "detection-results")
    confidence_threshold = float(os.getenv("CONFIDENCE_THRESHOLD", "0.4"))


settings = Settings()