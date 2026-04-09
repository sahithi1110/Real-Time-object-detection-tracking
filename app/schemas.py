from pydantic import BaseModel
from typing import List


class DetectionBox(BaseModel):
    track_id: int
    class_name: str
    confidence: float
    x1: int
    y1: int
    x2: int
    y2: int


class DetectionResponse(BaseModel):
    total_objects: int
    objects: List[DetectionBox]