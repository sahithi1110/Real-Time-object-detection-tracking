from ultralytics import YOLO
from app.config import settings


class ObjectDetector:
    def __init__(self):
        self.model = YOLO(settings.yolo_model_path)

    def detect(self, frame):
        results = self.model(frame, conf=settings.confidence_threshold, verbose=False)
        detections = []

        for result in results:
            names = result.names
            boxes = result.boxes

            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                confidence = float(box.conf[0].item())
                class_id = int(box.cls[0].item())
                class_name = names[class_id]

                detections.append({
                    "class_name": class_name,
                    "confidence": confidence,
                    "box": [int(x1), int(y1), int(x2), int(y2)]
                })

        return detections