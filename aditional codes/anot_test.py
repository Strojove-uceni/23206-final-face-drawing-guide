import cv2 as cv
import numpy as np
import math as m
import glob
import os


filetypes=["jpg","jpeg","png"]

files=[]
for ft in filetypes:
  files.extend(glob.glob("faces/*."+ft))
files.sort()

i=0
for f in files:
  i=i+1
  if os.path.isfile(f+".txt"):
    img=cv.imread(f)
    fa = open(f+".txt", "r")
    lines=fa.readlines()
    fa.close()

    print(f)
    #print(lines)
    for l in lines:
      p=l.split(";")
      if int(p[0])==0:
        cv.circle(img,(int(p[1]),int(p[2])),int(p[3]),(0,0,255),4)

      if int(p[0])==1:
        cv.ellipse(img,(int(p[1]),int(p[2])),(int(p[3]),int(p[4])),float(p[5]),0,360,(0,255,0),4)
    cv.imwrite(f+"_out.jpg",img)
    #imgre=cv.resize(img,[int(img.shape[1]*700/img.shape[0]),700])
    #cv.imshow('check',imgre)
    # key=cv.waitKey(5000)
    # if key==27:
    #   break
  print(i,"/",len(files))
  

