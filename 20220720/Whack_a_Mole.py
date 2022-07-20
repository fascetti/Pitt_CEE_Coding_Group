import Utils
import cv2
import mediapipe as mp
import time

capture = cv2.VideoCapture(0)
detector_object = Utils.HandDetector(detection=0.85)
listen = True
while True:
    success, img = capture.read()
    img = detector_object.find_hand(img, draw=True)
    landmark_list = detector_object.export_landmarks(img)

    img, listen, duration, speed = detector_object.start_game(img, landmark_list, listen)
    cTime = time.time()
    total_time = 0

    #while total_time <= duration:
    #   detector_object.play_game()

    #detector_object.randomize_points()
    #detector_object.display_mole()
    #detector_object.collision()
    #detector_object.update_score()

    cv2.imshow("Video Feed", img)
    cv2.waitKey(1)













