import cv2
import os


def convert_video_to_frames(video_path, frames_output_path, enhanced_output_path):
    # Create output directories if they don't exist
    os.makedirs(frames_output_path, exist_ok=True)
    os.makedirs(enhanced_output_path, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    frame_count = 0
    while cap.isOpened():
        # Read a frame from the video
        ret, frame = cap.read()

        if not ret:
            break

        # Check if the frame holds the same object (you may need to modify this condition)
        # For example, you can use some image processing techniques or object detection algorithms
        # to determine if the frame contains debris or not
        if frame_holds_same_object(frame):
            continue

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Save the frame image
        frame_path = os.path.join(frames_output_path, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_path, frame)

        # Save the enhanced image
        enhanced_path = os.path.join(enhanced_output_path, f"enhanced_frame_{frame_count}.jpg")
        cv2.imwrite(enhanced_path, gray_frame)

        frame_count += 1

    # Release the video capture object
    cap.release()

    print(f"Conversion completed. Total frames: {frame_count}")


def frame_holds_same_object(frame):
    # Implement your own logic to determine if the frame holds the same object
    # For demonstration purposes, this function always returns False
    return False


# Specify the paths
video_path = "D:\company\sattelite image\debris.mp4"
frames_output_path = "D:\company\sattelite image\out_frames"
enhanced_output_path = "D:\company\sattelite image\enhanced_frames"

# Call the function to convert the video to frames
convert_video_to_frames(video_path, frames_output_path, enhanced_output_path)
