import cv2
import datetime


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


# 构建视频保存的对象
# 为保存视频做准备，构建了一个对象，其中30为帧率，自己可按照需要修改
fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', '2')
out = cv2.VideoWriter("out.avi", fourcc, 30, (1280, 720))


while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Camera Huatec floor 6'
        datet = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 在视频画面写入文字
        frame = cv2.putText(
            frame, text, (10, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA
        )
        frame = cv2.putText(
            frame, datet, (10, 100), font, 1, (255, 255, 255), 2, cv2.LINE_AA
        )

        cv2.imshow('frame', frame)  # 显示视频
        out.write(frame)  # 保存视频

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
