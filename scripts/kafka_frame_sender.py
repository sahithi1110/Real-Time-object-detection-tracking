import cv2
from app.kafka_layer.producer import KafkaFrameProducer
from app.core.utils import frame_to_base64
from app.config import settings


def main():
    producer = KafkaFrameProducer()
    capture = cv2.VideoCapture(0)

    if not capture.isOpened():
        print("Could not open webcam")
        return

    while True:
        success, frame = capture.read()
        if not success:
            break

        payload = {
            "frame": frame_to_base64(frame)
        }

        producer.send(settings.kafka_input_topic, payload)

        cv2.imshow("Sending Frames to Kafka", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()