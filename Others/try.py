import cv2
import mediapipe as mp

# Create a MediaPipe pose estimator
pose_estimator = mp.solutions.pose.Pose()

v = '2.mp4'

# Load the video file
video = cv2.VideoCapture(v)

# Process each frame in the video file
while video.isOpened():

    # Read the frame
    success, image = video.read()

    # Check if the frame is empty
    if not success:
        break

    # Preprocess the image for MediaPipe
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Perform pose estimation
    results = pose_estimator.process(image)

    # Get the keypoints from the results
    keypoints = results.pose_landmarks.landmark

    # Draw the keypoints on the image
    for keypoint in keypoints:
        x = int(keypoint.x * image.shape[1])
        y = int(keypoint.y * image.shape[0])
        cv2.circle(image, (x, y), 3, (0, 255, 0), -1)

    # Display the output image
    cv2.imshow("Output", image)

    # Wait for a key to be pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
video.release()

# Destroy all windows
cv2.destroyAllWindows()