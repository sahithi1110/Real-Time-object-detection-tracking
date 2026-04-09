import os
import uuid
import cv2

from fastapi import APIRouter, UploadFile, File
from app.schemas import DetectionResponse, DetectionBox
from app.services.video_service import VideoProcessor
from app.core.pipeline import DetectionPipeline

router = APIRouter()
video_processor = VideoProcessor()
pipeline = DetectionPipeline()


@router.get("/")
def health_check():
    return {"message": "API is running fine"}


@router.post("/detect/image", response_model=DetectionResponse)
async def detect_from_image(file: UploadFile = File(...)):
    contents = await file.read()

    temp_name = f"temp_{uuid.uuid4().hex}.jpg"
    with open(temp_name, "wb") as image_file:
        image_file.write(contents)

    frame = cv2.imread(temp_name)
    os.remove(temp_name)

    tracked_objects = pipeline.run(frame)

    response_objects = []
    for item in tracked_objects:
        x1, y1, x2, y2 = item["box"]
        response_objects.append(
            DetectionBox(
                track_id=item["track_id"],
                class_name=item["class_name"],
                confidence=item["confidence"],
                x1=x1,
                y1=y1,
                x2=x2,
                y2=y2
            )
        )

    return DetectionResponse(
        total_objects=len(response_objects),
        objects=response_objects
    )


@router.post("/detect/video")
async def detect_from_video(file: UploadFile = File(...)):
    input_path = f"input_{uuid.uuid4().hex}.mp4"
    output_path = f"sample_output/output_{uuid.uuid4().hex}.mp4"

    with open(input_path, "wb") as video_file:
        video_file.write(await file.read())

    video_processor.process_video_file(input_path, output_path)
    os.remove(input_path)

    return {"message": "Video processed successfully", "output_path": output_path}