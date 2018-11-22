#导入cv模块
import cv2
import os
face_xml=r"D:\project\ffw\python\lbpcascade_frontalface.xml"
eye_xml=r"D:\project\ffw\opencv-master\data\haarcascades\haarcascade_eye.xml"
#读取图像，支持 bmp、jpg、png、tiff 等常用格式
img = cv2.imread(r"C:\\Users\\temp\\Desktop\\q.jpg")
print("exists:",os.path.exists(face_xml))
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_cascade=cv2.CascadeClassifier(face_xml)
eye_cascade=cv2.CascadeClassifier(eye_xml)
faces=face_cascade.detectMultiScale(gray_img,
                                    #scaleFactor=1.15,
                                    minNeighbors=5,
                                    #maxSize=(3000,3000),
                                    #flags=cv2.CASCADE_SCALE_IMAGE
                                    )
eyes=eye_cascade.detectMultiScale(gray_img,minNeighbors=5)
print(len(faces))  
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
for (x,y,w,h) in eyes:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
#创建窗口并显示图像
cv2.namedWindow("Image")
cv2.imshow("Image",img)

#cv2.namedWindow("Image_GRAY")
#cv2.imshow("Image_GRAY",gray_img)
cv2.waitKey(0)
#释放窗口
cv2.destroyAllWindows()