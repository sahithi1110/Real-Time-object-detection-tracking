import math


class SimpleTracker:
    def __init__(self, max_distance=60):
        self.max_distance = max_distance
        self.next_track_id = 1
        self.active_tracks = {}

    def _get_center(self, box):
        x1, y1, x2, y2 = box
        return ((x1 + x2) // 2, (y1 + y2) // 2)

    def _distance(self, point_a, point_b):
        return math.sqrt((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2)

    def update(self, detections):
        updated_tracks = {}
        used_track_ids = set()

        for detection in detections:
            current_box = detection["box"]
            current_center = self._get_center(current_box)

            matched_track_id = None
            smallest_distance = float("inf")

            for track_id, track_data in self.active_tracks.items():
                if track_id in used_track_ids:
                    continue

                old_center = self._get_center(track_data["box"])
                distance = self._distance(current_center, old_center)

                if distance < self.max_distance and distance < smallest_distance:
                    smallest_distance = distance
                    matched_track_id = track_id

            if matched_track_id is None:
                matched_track_id = self.next_track_id
                self.next_track_id += 1

            detection["track_id"] = matched_track_id
            updated_tracks[matched_track_id] = detection
            used_track_ids.add(matched_track_id)

        self.active_tracks = updated_tracks
        return list(updated_tracks.values())