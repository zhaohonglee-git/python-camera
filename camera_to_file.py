import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


# 默认分辨率为640*480
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('myvideo.mp4', fourcc, 30.0, (1280, 720))

while True:

    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    out.write(frame)
    cv2.imshow('camera', frame)

    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
