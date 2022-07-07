import Utils
import cv2

capture = cv2.VideoCapture(0)
detector_object = Utils.hand_detector(detection=0.85)

while True:
    success, img = capture.read()
    img = detector_object.find_hand(img)
    # landmarks = detector_object.export_landmarks(img)
    # res = detector_object.process_landmarks(img)

