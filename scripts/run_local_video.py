import cv2
from app.services.video_service import VideoProcessor


def main():
    processor = VideoProcessor()
    capture = cv2.VideoCapture(0)

    if not capture.isOpened():
        print("Could not open webcam")
        return

    while True:
        success, frame = capture.read()
        if not success:
            break

        _, processed_frame = processor.process_frame(frame)
        cv2.imshow("Real-Time Detection", processed_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()