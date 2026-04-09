import cv2
from app.core.pipeline import DetectionPipeline
from app.core.utils import draw_boxes


class VideoProcessor:
    def __init__(self):
        self.pipeline = DetectionPipeline()

    def process_frame(self, frame):
        tracked_objects = self.pipeline.run(frame)
        output_frame = draw_boxes(frame.copy(), tracked_objects)
        return tracked_objects, output_frame

    def process_video_file(self, input_path, output_path):
        capture = cv2.VideoCapture(input_path)

        if not capture.isOpened():
            raise ValueError("Could not open input video")

        width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = capture.get(cv2.CAP_PROP_FPS)

        writer = cv2.VideoWriter(
            output_path,
            cv2.VideoWriter_fourcc(*"mp4v"),
            fps if fps > 0 else 25,
            (width, height)
        )

        while True:
            success, frame = capture.read()
            if not success:
                break

            _, processed_frame = self.process_frame(frame)
            writer.write(processed_frame)

        capture.release()
        writer.release()