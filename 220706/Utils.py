import mediapipe as mp
import cv2
import time

class hand_detector():
    def __init__(self, mode=False, max_hands=2, complexity=1, detection=0.5, tracking=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.complexity = complexity
        self.detection = detection
        self.tracking = tracking

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.max_hands, self.complexity, self.detection, self.tracking)
        self.mpDraw = mp.solutions.drawing_utils

    def find_hand(self, img, draw=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:  # Cycles over all landmarks on one hand
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def export_landmarks(self, img, draw=False):
        lm_list = []
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for l_id, lm in enumerate(handLms.landmark):  # Cycles through all the landmarks in each hand
                    height, width, c = img.shape
                    cx_ = int(lm.x * width)
                    cy_ = int(lm.y * height)
                    lm_list.append([l_id, cx_, cy_])
                if draw:
                    cv2.circle(img, (cx_, cy_), 10, (255, 0, 0), cv2.FILLED)
        return lm_list
    