#!/usr/bin/python3

import cv2 as cv
import numpy as np
import math as m
import glob
import os


def getFilename():
  filetypes=["jpg","jpeg","png"]

  files=[]
  for ft in filetypes:
    files.extend(glob.glob("data/*."+ft))
  files.sort()

  for f in files:
    if not os.path.isfile(f+".txt"):
      return f


filename=getFilename()
print(filename)
img=cv.imread(filename)
imgre=cv.resize(img,[int(img.shape[1]*600/img.shape[0]),600])
font = cv.FONT_HERSHEY_SIMPLEX

#pole elementov:
#kružnica [0, x, y, r]
#elipsa [1, x, y, a, b, uhel]
elementy=[]

cv.namedWindow('image',cv.WINDOW_AUTOSIZE)

def dst(x,y):
  dx=x[0]-y[0]
  dy=x[1]-y[1]
  return m.sqrt(dx*dx+dy*dy)

key=-1
selected=-1

def mouseCallback(event,x,y,flags,param):
    global key
    global selected
    if event == cv.EVENT_LBUTTONDOWN:
      if key==99:
        elementy.append([0,x,y,10])
        key=-1     
        selected=len(elementy)-1
        draw()
        return

      if key==101:
        elementy.append([1,x,y,20,10,0])
        key=-1
        selected=len(elementy)-1    
        draw()
        return
      
      for i,e in enumerate(elementy):
        if e[0]==0:
          if dst([e[1],e[2]],[x,y])<e[3]:
            selected=i
            draw() 
        if e[0]==1:
          if dst([e[1],e[2]],[x,y])<min(e[3],e[4]):
            selected=i
            draw() 

    if selected!=-1:
      if event == cv.EVENT_MOUSEMOVE:
        if flags==8:
          elementy[selected][1]=x
          elementy[selected][2]=y
          draw()
        if flags==16:
          if elementy[selected][0]==0:
            elementy[selected][3]=int(dst([elementy[selected][1],elementy[selected][2]],[x,y]))
            draw()

          if elementy[selected][0]==1:
            dx=elementy[selected][1]-x
            dy=elementy[selected][2]-y
            r=elementy[selected][5]/180*m.pi
            s=m.sin(-r)
            c=m.cos(-r)

            elementy[selected][3]=abs(int(dx*c-dy*s))
            elementy[selected][4]=abs(int(dx*s+dy*c))
            draw()


        if flags==24:
          if elementy[selected][0]==1:
            elementy[selected][5]=m.atan2(y-elementy[selected][2],x-elementy[selected][1])/m.pi*180
            draw()


cv.setMouseCallback('image',mouseCallback)

def draw():
  out=np.copy(imgre)
  for i,e in enumerate(elementy):
    color=(0,0,255)
    if selected==i:
      color=(255,0,0)
    if e[0]==0:
      cv.circle(out,(e[1],e[2]),e[3],color,2)
    if e[0]==1:
      cv.ellipse(out,(e[1],e[2]),(e[3],e[4]),e[5],0,360,color,2)


  text=""
  if selected!=-1:
    text="S"
  if key==99:
    text="C"
  if key==101:
    text="E"
  cv.putText(out,text,(10,50), font, 2,(0,255,0),2,cv.LINE_AA)
  cv.imshow('image',out)


draw()
while key!=27:
  key=cv.waitKey(5000)
  draw()
  if key==114:
    elementy=[]
    draw()

  if key==113:
    selected=-1
    draw()

  if key==13:
    #save current  
    f = open(filename+".txt", "w")
    for e in elementy:

      count=4
      if e[0]==1:
        count=5
      for i in range(1,count):
        e[i]=int(e[i]*img.shape[1]/imgre.shape[1])

      for i in e:      
        f.write(str(i)+";")
      f.write("\n")

    f.close()
    #load next
    filename=getFilename()
    print(filename)
    img=cv.imread(filename)
    imgre=cv.resize(img,[int(img.shape[1]*600/img.shape[0]),600])
    elementy=[]
    draw()

  print(key)



