import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    _, th_1 = cv2.threshold(frame, 200, 255, cv2.THRESH_BINARY_INV)  # for black backgrounds - binary - global
    _, th_2 = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY)  # for white backgrounds - binary - global
    # Our operations on the frame come here


    # Display the resulting frame
    cv2.imshow('th_1',th_1)
    cv2.imshow('th_2',th_2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()