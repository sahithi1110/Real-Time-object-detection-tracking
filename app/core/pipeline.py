from app.core.detector import ObjectDetector
from app.core.tracker import SimpleTracker


class DetectionPipeline:
    def __init__(self):
        self.detector = ObjectDetector()
        self.tracker = SimpleTracker()

    def run(self, frame):
        detections = self.detector.detect(frame)
        tracked_objects = self.tracker.update(detections)
        return tracked_objects