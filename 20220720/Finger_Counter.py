import Utils
import cv2
import mediapipe as mp

capture = cv2.VideoCapture(0)
detector_object = Utils.HandDetector(detection=0.85)

while True:
    success, img = capture.read()
    img = detector_object.find_hand(img, draw=True)
    landmark_list = detector_object.export_landmarks(img)
    finger_count = 0
    if landmark_list:
        for i in [8, 12, 16, 20]:  # Taking care of my four fingers
            if landmark_list[i][1] < landmark_list[i-3][1]:
                finger_count += 1
        if landmark_list[4][0] > landmark_list[2][0]:
            finger_count += 1
    overlay_image_name = str(finger_count)
    img[0:240, 0:170] = cv2.imread(f'Images/{overlay_image_name}.png')
    cv2.rectangle(img, (0, 300), (170, 500), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, str(finger_count), (35, 450), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 10)
    cv2.imshow("Video Feed", img)
    cv2.waitKey(1)













