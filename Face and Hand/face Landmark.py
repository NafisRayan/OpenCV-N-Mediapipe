import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh

def detect_face_landmarks_from_camera():

  face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5, 
    min_tracking_confidence=0.5)

  cap = cv2.VideoCapture(0)

  while True:
    
    ret, frame = cap.read()

    # Convert BGR to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Make detection
    results = face_mesh.process(frame_rgb)

    # Draw landmarks
    if results.multi_face_landmarks:
      for face_landmarks in results.multi_face_landmarks:
        
        for landmark in face_landmarks.landmark:
          x = int(landmark.x * frame.shape[1]) 
          y = int(landmark.y * frame.shape[0])
          cv2.circle(frame, (x,y), 2, (0,255,0), -1)

    cv2.imshow('Face Mesh', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  cap.release()
  cv2.destroyAllWindows()

detect_face_landmarks_from_camera()


