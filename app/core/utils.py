import cv2
import base64
import numpy as np


def frame_to_base64(frame):
    success, buffer = cv2.imencode(".jpg", frame)
    if not success:
        raise ValueError("Could not encode frame")
    return base64.b64encode(buffer).decode("utf-8")


def base64_to_frame(frame_string):
    frame_bytes = base64.b64decode(frame_string)
    frame_array = np.frombuffer(frame_bytes, dtype=np.uint8)
    frame = cv2.imdecode(frame_array, cv2.IMREAD_COLOR)
    return frame


def draw_boxes(frame, tracked_objects):
    for item in tracked_objects:
        x1, y1, x2, y2 = item["box"]
        class_name = item["class_name"]
        track_id = item["track_id"]
        confidence = item["confidence"]

        label = f"{class_name} | ID {track_id} | {confidence:.2f}"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(
            frame,
            label,
            (x1, max(y1 - 8, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (0, 255, 0),
            2
        )
    return frame