from app.core.pipeline import DetectionPipeline


class StreamProcessor:
    def __init__(self):
        self.pipeline = DetectionPipeline()

    def process_frame(self, frame):
        return self.pipeline.run(frame)