from ultralytics import YOLO
import cv2
import numpy as np

# Load the YOLO model with full path
model = YOLO('D:/PlayerMapping/best.pt')

# Load the video with full path
video = cv2.VideoCapture('D:/PlayerMapping/15sec_input_720p.mp4')

if not video.isOpened():
    print("Error: Video failed to open")
else:
    print("Video opened successfully")

# List of unique names for players
unique_names = ["John", "Mike", "Sarah", "Emma", "David", "Lisa", "Tom", "Anna", 
                "Chris", "Sophie", "James", "Emily", "Alex", "Rachel", "Peter"]
name_index = 0  # Index to track the next available name

# Dictionary to store player IDs and their last known positions/names
player_tracker = {}  # Maps player index to name and position

while True:
    ret, frame = video.read()

    if not ret:
        print("End of video or frame read failed")
        break

    # Detect players in the frame
    results = model(frame)

    # Process detections
    for i, result in enumerate(results):
        boxes = result.boxes.xyxy
        for j, box in enumerate(boxes):
            x1, y1, x2, y2 = map(int, box[:4])
            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2

            # Check if this player was seen before
            player_key = None
            for key, (name, last_x, last_y) in player_tracker.items():
                # Simple distance check to re-identify (adjust threshold as needed)
                if abs(center_x - last_x) < 50 and abs(center_y - last_y) < 50:
                    player_key = key
                    break

            if player_key is None:  # New player
                if name_index < len(unique_names):
                    player_tracker[i] = (unique_names[name_index], center_x, center_y)
                    name_index += 1
                else:
                    player_tracker[i] = (f"Player_{name_index - len(unique_names) + 1}", center_x, center_y)
                    name_index += 1
            else:  # Update last seen position
                player_tracker[i] = (player_tracker[player_key][0], center_x, center_y)

            # Draw rectangle and name
            name = player_tracker[i][0]
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, name, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Re-Identification', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):  # Press 'q' to quit
        break

# Release video and close windows
video.release()
cv2.destroyAllWindows()