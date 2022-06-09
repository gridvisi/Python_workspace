"""
https://zhuanlan.zhihu.com/p/422527346

视频流人脸识别
需要通过命令 pip install opencv-python face-recognition numpy  安装依赖项
"""
import face_recognition
import cv2
import numpy as np

# 获取摄像头
video_capture = cv2.VideoCapture(0)

# 加载图片获取脸部特征
obama_image = face_recognition.load_image_file('obama.jpg')
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
qianfeng_image = face_recognition.load_image_file('qianfeng.jpg')
qianfeng_face_encoding = face_recognition.face_encodings(qianfeng_image)[0]

# 保存脸部特征和对应的名字
known_face_encodings = [
    obama_face_encoding,
    qianfeng_face_encoding
]
known_face_names = ['Barack Obama', 'qianfeng']

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # 从视频中读取一帧数据
    ret, frame = video_capture.read()

    # 调整为原始尺寸的四分之一（加速处理）
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # BGR转成RGB
    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        # 找到所有的人脸位置和脸部特征保存在列表中
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # 比较脸部特征
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # 找到匹配成功的下标对应的名字
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            # 通过距离判定最佳匹配并获取对应的名字
            # face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            # best_match_index = np.argmin(face_distances)
            # if matches[best_match_index]:
            #    name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # 显示结果
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # 恢复正常的尺寸
        top, right, bottom, left = top * 4, right * 4, bottom * 4, left * 4
        # 绘制一个标识人脸的矩形框
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # 绘制一个填写名字的矩形框
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    # 按键盘上的q键退出窗口
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()