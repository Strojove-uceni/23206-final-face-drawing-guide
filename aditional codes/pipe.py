import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2 as cv
import numpy as np
import glob
import os

#!wget -O face_landmarker_v2_with_blendshapes.task -q https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task

#mediapipe

#  Create an FaceLandmarker object.
base_options = python.BaseOptions(model_asset_path='face_landmarker_v2_with_blendshapes.task')
options = vision.FaceLandmarkerOptions(base_options=base_options,
                                       output_face_blendshapes=True,
                                       output_facial_transformation_matrixes=True,
                                       num_faces=1)
detector = vision.FaceLandmarker.create_from_options(options)

#device = next(model.parameters()).device

def getFiles():
    filetypes=["jpg","jpeg","png"]
    files=[]
    for ft in filetypes:
        files.extend(glob.glob("faces/*."+ft))
    files.sort()
    return files

files=getFiles()
key=0
frame=0
while key!=27:
    f=files[frame]
    print("Processing file: {} ".format(f),frame,"/",len(files))
    image = mp.Image.create_from_file(f)

    
    detection_result = detector.detect(image)
    lmks = detection_result.face_landmarks
    xyz_coordinates = [[point.x, point.y, point.z] for landmark_list in lmks for point in landmark_list]

    for u,p in enumerate(xyz_coordinates):
      cord=np.multiply(np.array(p),np.array([image.width,image.height,image.width])).astype(int)
      xyz_coordinates[u]=cord
      
    imgCV=cv.cvtColor(image.numpy_view(), cv.COLOR_RGB2BGR)
    oh=imgCV.shape[0]
    ow=imgCV.shape[1]
    h=600
    coef=600.0/imgCV.shape[0]
    w=int(imgCV.shape[1]*coef)
    rimg = cv.resize(imgCV,[w,h])
    for p in xyz_coordinates:
        cv.circle(rimg, (int(p[0]*coef),int(p[1]*coef)),radius=3, color=(0, 255, 255), thickness=-1)
    cv.imshow("bjhb",rimg)
    key=cv.waitKey(0)
    print(key)
    if key==112:
        print("petrzel...")
        os.rename(f,f+"_petrzel")
        os.rename(f+".txt", f+".txt"+"_petrzel")
        files=getFiles()

    if key==113:
        frame=frame-1

    if key==119:
        frame=frame+1

    if frame<0:
        frame = 0

    if frame >= len(files):
        frame=len(files)-1
    
