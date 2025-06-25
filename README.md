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


- **Next Steps with More Time/Resources**: 
  - Use machine learning to learn player features (e.g., jersey patterns) for better matching.
  - Optimize for real-time performance by reducing processing time per frame.

