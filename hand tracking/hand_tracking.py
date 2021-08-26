import mediapipe as mp
from mediapipe.python.solutions import hands
import cv2
import keyboard, time

# Handling our video object, zero value mean camera number 1
cap = cv2.VideoCapture(0)

# Handling Hands object from mediapipe libairy
mpHands = mp.solutions.hands
hands = mpHands.Hands()

mpDraw = mp.solutions.drawing_utils

# pTime = 0
# cTime = 0
tipIds = [4,8,12,16,20] 
count=0
while True:
    success, img = cap.read()
    # Coverting into RGB, becouse class {hands} only uses RGB images
    imgRGP = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results= hands.process(imgRGP)
    lmList=[]
    
    # Check if we have multiple hands or not
    if results.multi_hand_landmarks:
        # Draw Points in Hands {21 LandMarks}
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx = int(lm.x * w)
                cy = int(lm.y * h)
                lmList.append([id , cx , cy])
                
                # Draw Circle on every handmark
                cv2.circle(img,(cx, cy), 10, (255,0,255), cv2.FILLED)
            
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    if len(lmList) !=0: 
        if abs(lmList[7][2] - lmList[4][2]) <= 35 :
            count+=1  
            if count == 1:        
                keyboard.press_and_release('space')
                time.sleep(0.15)
        else:                                    
            count=0
    
    

    cv2.imshow("close camera by pressing 'q'", img)
    cv2.waitKey(1)

        