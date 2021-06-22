import onnxruntime as ort
import cv2
import numpy as np

sess= ort.InferenceSession("mobilenet_v2_0.25_160x160x3_age_smile_gender_glass_beauty_eyegaze_v1_epoch_199_val_loss0.onnx")
inputName = sess.get_inputs()[0].name

cameraCapture = cv2.VideoCapture(0)
    # cv2级联分类器CascadeClassifier,xml文件为训练数据
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

    # 读取数据
success, frame = cameraCapture.read()

while success and cv2.waitKey(1) == -1:
        # 读取数据
    ret, img = cameraCapture.read()
        # 进行人脸检测
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
        # 绘制矩形框
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # 设置显示窗口
        crop_img = img[y:y+h,x:x+w,:]

        crop_img=cv2.resize(crop_img,(160,160))
        zhuanzhi = np.transpose(crop_img, (2, 0, 1)).astype('float32')  #转置

        out= np.expand_dims(zhuanzhi,0)  #降维

        onnxout = sess.run(None, {inputName : out})
        if onnxout is None:
            gender='女'
        else:
            gender='男'
        #print(onnxout)
        age = int(onnxout[0][0][0] * 100-10)    # 推算年龄

        print("检测到受困者，年龄大约为",(age),"岁","性别为",gender)
        cv2.putText(img, "age:"+str(age),(x+w,y+h),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.namedWindow('camera', 0)

        # 显示处理后的视频
    cv2.imshow('camera', img)
        # 读取数据
    success, frame = cameraCapture.read()
    # 释放视频
cameraCapture.release()
    # 释放所有窗口
cv2.destroyAllWindows()