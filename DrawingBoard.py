from turtle import position
import cv2
import numpy as np
import time
import os
import HandModule as htm

brushThickness = 25
eraserThickness = 100


folderPath = "D:\VS CODES\REBUILD VI DRAW\Header"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))
header = overlayList[0]
drawColor = (0, 0, 0)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.handDetector(detectionCon=0.1,maxHands=1)
xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

while True:

    # 1. Import image
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # 2. Find Hand Landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:

        # print(lmList)
        # tip of index and middle fingers
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # 3. Check which fingers are up
        fingers = detector.fingersUp()
        # print(fingers)

        # 4. If Selection Mode - Two finger are up
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            # print("Selection Mode")
            # # Checking for the click
            if y1 < 120:
                if 150 < x1 < 200:
                    header = overlayList[1]
                    drawColor = (26, 26, 26)
                elif 200 < x1 < 250:
                    header = overlayList[2]
                    drawColor = (255, 255, 255)
                elif 250 < x1 < 300:
                    header = overlayList[3]
                    drawColor = (0, 0, 255)
                elif 300 < x1 < 350:
                    header = overlayList[4]
                    drawColor = (0, 255, 255)
                elif 350 < x1 < 400:
                    header = overlayList[5]
                    drawColor = (0, 255, 0)
                elif 400 < x1 < 450:
                    header = overlayList[6]
                    drawColor = (255, 0, 0)
                elif 450 < x1 < 500:
                    header = overlayList[7]
                    drawColor = (204, 0, 153)
                elif 500 < x1 < 550:
                    header = overlayList[8]
                    drawColor = (122,49,14)
                elif 550 < x1 < 600:
                    header = overlayList[9]
                    drawColor = (255, 255, 0)
                elif 600 < x1 < 650:
                    header = overlayList[10]
                    drawColor = (255, 179, 255)
                elif 650 < x1 < 700:
                    header = overlayList[11]
                    drawColor = (163, 163, 194)
                elif 700 < x1 < 750:
                    header = overlayList[12]
                    drawColor = (0, 102, 34)
                elif 750 < x1 < 800:
                    header = overlayList[13]
                    drawColor = (255, 108, 0)
                elif 800 < x1 < 850:
                    header = overlayList[14]
                    drawColor = (255, 152, 152)
                elif 850 < x1 < 900:
                    header = overlayList[15]
                    drawColor = (77, 0, 77)
                elif 900 < x1 < 950:
                    header = overlayList[16]
                    drawColor = (51, 51, 77)
                elif 950 < x1 < 1000:
                    header = overlayList[17]
                    drawColor = (0, 51, 0)
                elif 1000 < x1 < 1050:
                    header = overlayList[18]
                    drawColor = (255, 179, 179)
                elif 1050 < x1 < 1280:
                    header = overlayList[19]
                    drawColor = (0, 0, 0)
            cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)

        # 5. If Drawing Mode - Index finger is up
        if fingers[1] and fingers[2] == False:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
            # print("Drawing Mode")
            if xp == 0 and yp == 0:
                xp, yp = x1, y1
                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)

            if drawColor == (0, 0, 0):
                 cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                 cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
            
            else:
                 cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                 cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)

            xp, yp = x1, y1


        # # Clear Canvas when all fingers are up
        #if all (x >= 1 for x in fingers):
             #imgCanvas = np.zeros((720, 1280, 3), np.uint8)

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img,imgInv)
    img = cv2.bitwise_or(img,imgCanvas)


    # Setting the header image
    img[0:120, 0:1280] = header
    img = cv2.addWeighted(img,0.5,imgCanvas,0.5,0)
    cv2.imshow("Camera Feed", img)
    cv2.imshow("Drawing Board", imgCanvas)
    #cv2.imshow("Inv", imgInv)
    cv2.waitKey(1)
