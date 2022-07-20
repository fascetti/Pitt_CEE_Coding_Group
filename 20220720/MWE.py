import cv2
import mediapipe as mp
import time
import numpy as np
from numpy.linalg import norm

capture = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0

while True:
    success, img = capture.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    dist = 0
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:  # Cycles over all landmarks on one hand
            cx = []
            cy = []
            for l_id, lm in enumerate(handLms.landmark):  # Cycles through all the landmarks in each hand
                if l_id in [8, 4]:
                    height, width, c = img.shape
                    cx_ = int(lm.x * width)
                    cy_ = int(lm.y * height)
                    cx.append(cx_)
                    cy.append(cy_)
                    cv2.circle(img, (cx_, cy_), 10, (0, 0, 255), cv2.FILLED)
            dist = norm([cx[1] - cx[0], cy[1] - cy[0]])
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, 'FPS: ' + str(int(fps)), (30, 80), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)  # Project FPS on Screen
    cv2.putText(img, 'Dist: ' + str(int(dist)), (350, 80), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0),
                2)  # Project FPS on Screen
    cv2.imshow("Video", img)
    cv2.waitKey(1)














