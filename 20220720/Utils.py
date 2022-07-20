import mediapipe as mp
import cv2
#import time


class HandDetector():
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

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:  # Cycles over all landmarks on one hand
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def export_landmarks(self, img, draw=False, list_landmarks=[]):
        lm_list = []
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for l_id, lm in enumerate(handLms.landmark):  # Cycles through all the landmarks in each hand
                    height, width, c = img.shape
                    cx_ = int(lm.x * width)
                    cy_ = int(lm.y * height)
                    lm_list.append([cx_, cy_])
                #if draw:
                #    cv2.circle(img, (cx_, cy_), 10, (255, 0, 0), cv2.FILLED)
        return lm_list

    def start_game(self, img, lm_list, listen, duration = 30, speed = 1):

        if listen:
            height, width, c = img.shape
            cv2.rectangle(img, (int(0.8*width), int(0.01*width)), (int(0.99*width), int(0.2*height)), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "Move finger", (int(0.8*width), int(0.05*height)), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
            cv2.putText(img, "here to start", (int(0.8*width), int(0.15*height)), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
            if lm_list:
                if lm_list[8][0] > int(0.8*width) and lm_list[8][1] < int(0.2*height):
                    listen = False
        return img, listen, duration, speed
