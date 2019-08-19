import cv2

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# You can inform the id of the property that you want to set a value
# in this case i'm settting a width (3) and a height(4)
cap.set(3, 1280)
cap.set(4, 720)

print(cap.get(3))
print(cap.get(4))

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break