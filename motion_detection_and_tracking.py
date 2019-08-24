import cv2
import numpy as np

cap = cv2.VideoCapture('./data/vtest.avi')

ret, first_frame = cap.read()
ret, second_frame = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(first_frame, second_frame)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, width, height) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 700:
            continue
        
        cv2.rectangle(first_frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
        cv2.putText(first_frame, "Status: {}".format('Movement'), (15, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # cv2.drawContours(first_frame, contours, -1, (0, 255, 0), 2)

    cv2.imshow("inter", first_frame)

    first_frame = second_frame
    ret, second_frame = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()