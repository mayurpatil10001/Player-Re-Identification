# Player Re-Identification in Sports Footage

This repository contains code to perform player re-identification in a single video feed using a YOLO model.

## How to Set Up and Run the Code

1. **Install Anaconda**: Ensure Anaconda is installed on your system (used here at `D:/Anaconda/`).
2. **Create or Use an Environment**: Activate the base environment or create a new one:
3. **Install Dependencies**: Install required Python packages:
4. **Download Files**:
- Video: `15sec_input_720p.mp4` from [this link](https://drive.google.com/drive/folders/1Nx6H_n0UUI6L-6i8WknXd4Cv2c3VjZTP?usp=sharing).
- Model: `best.pt` from [this link](https://drive.google.com/file/d/1-5fOSHOSB9UXyP_enOoZNAMScrePVcMD/view) (save as `best.pt`).
- Place both files in `D:\PlayerMapping\`.
5. **Run the Script**: Navigate to the project folder and execute:
6. **Usage**: A window will display the video with player detections. Press `q` to quit.

## Dependencies or Environment Requirements
- **Python**: Version 3.13.5 (or compatible) via Anaconda.
- **Libraries**:
- `ultralytics` (for YOLO model)
- `opencv-python` (for video processing)
- `numpy` (for numerical operations)
- **Operating System**: Windows (tested on the current setup).

# Player Re-Identification Report

## Your Approach and Methodology
- **Objective**: The task was to identify players in a 15-second video (`15sec_input_720p.mp4`) and ensure players who go out of frame and reappear retain the same identity.
- **Approach**: Used a pre-trained YOLOv11 model (`best.pt`) to detect players in each frame. Implemented a simple tracking mechanism using the center coordinates of bounding boxes to re-identify players based on a distance threshold (50 pixels).
- **Methodology**: Processed the video frame-by-frame, assigned unique names (e.g., "John," "Mike") from a predefined list, and updated player identities when they reappeared within the threshold distance.

## Techniques You Tried and Their Outcomes
- **Player Detection**: Utilized the YOLO model to detect players, which successfully drew bounding boxes around them.
- **Re-Identification**: Implemented a distance-based check to match players who re-entered the frame. Initial tests showed reasonable re-identification for players with consistent movement, but accuracy varied with rapid movements.
- **Naming**: Assigned unique names from a list, ensuring each new player received a distinct identity. Fallback to `Player_X` was included if the name list was exhausted.

## Challenges Encountered
- **Threshold Sensitivity**: The 50-pixel distance threshold sometimes misidentified players with overlapping paths or rapid movements.
- **Model Limitations**: The YOLO model occasionally missed detections, especially with occlusions or small player sizes.
- **Display Issues**: Initially faced issues with video windows not opening, resolved by ensuring correct file paths and OpenCV setup.

## If Incomplete, Describe What Remains and How You Would Proceed with More Time/Resources
- **Current Status**: The basic re-identification works, but accuracy needs improvement.
- **Remaining Tasks**: 
  - Fine-tune the distance threshold or implement a more robust tracking algorithm (e.g., Deep SORT).
  - Enhance the model with additional training data for better detection in challenging scenarios.
- **Next Steps with More Time/Resources**: 
  - Use machine learning to learn player features (e.g., jersey patterns) for better matching.
  - Optimize for real-time performance by reducing processing time per frame.

