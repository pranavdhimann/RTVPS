# Space Picker Code

import cv2
import pickle

width, height = 107, 48

try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except FileNotFoundError:
    posList = []

def mouseClick(events, x, y, flags, params):
    global posList
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    elif events == cv2.EVENT_RBUTTONDOWN:
        posList = [pos for pos in posList if not (pos[0] < x < pos[0] + width and pos[1] < y < pos[1] + height)]

    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)

cv2.namedWindow("Image", cv2.WINDOW_GUI_NORMAL)
cv2.setMouseCallback("Image", mouseClick)

while True:
    img = cv2.imread('carParkImg.png')
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    if key == 27:  # Press 'Esc' to exit the loop
        break

cv2.destroyAllWindows()
