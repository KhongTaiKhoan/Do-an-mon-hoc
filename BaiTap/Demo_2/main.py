import  pandas as pd
import numpy as np
from tkinter import *
from PIL import Image,ImageDraw
import cv2 , joblib
from sklearn.svm import SVC
import  sklearn
from train import huanLuyen





###########################################
####### DAY LA PHAN CODE GIAO DIEN ########
###########################################
print('The scikit-learn version is {}.'.format(sklearn.__version__))
height = 400;
width  = 300;
tk = Tk();
tk.title("Demo SVM");

#---- LOAD MODEL
clf = joblib.load("mo-hinh-svm-1.joblib");
# huanLuyen();

#----  CAC HAM XU LY XU KIEN
def paint(event):
    x1,y1 = event.x-10,event.y-10;
    x2,y2 = event.x+10,event.y+10;
    canvas.create_oval(x1,y1,x2,y2,fill="white",outline="white");
    draw.ellipse((x1,y1,x2,y2),fill="white",outline="white");

def Xoa():
    global img,draw;
    canvas.delete("all");
    img =Image.new("RGB",(230,230),"black");
    draw = ImageDraw.Draw(img);

def kt():
    anhXam = cv2.cvtColor(np.array( img.resize( (28,28),Image.ANTIALIAS )),cv2.COLOR_BGR2GRAY);

    # cv2.imshow("Show anh xam",anhXam);
    hog = cv2.HOGDescriptor(_winSize=(28, 28),
                            _blockSize=(8, 8),
                            _blockStride=(4, 4),
                            _cellSize=(4, 4),
                            _nbins=9);
    arr = hog.compute(anhXam, None, None)
    arr = np.reshape(arr, (1, arr.shape[0]))
    lblKQ['text'] = "";
    lblKQ['text']="Ket qua: "+ str(int(clf.predict(arr)) );


#--- TAO Canvas
canvas = Canvas(tk,height=230,width=230,bg="black");
canvas.pack(side=TOP);
canvas.bind("<B1-Motion>", paint);
img = Image.new("RGB",(230,230),"black");
draw = ImageDraw.Draw(img);


#---Tao button dieu khien
frame=Frame(tk);
frame.pack();
btnXoa = Button (frame,text="Xóa",command = Xoa);
btnXoa.pack(side=LEFT,padx=10,pady=20);

btnKiemTra = Button (frame,text="kiểm tra",command = kt);
btnKiemTra.pack(side=LEFT);

#---TAO KHUNG KET QUA

frameBt = Frame(tk);
frameBt.pack(side=BOTTOM)
lblKQ = Label(frameBt,text="Ket qua: ",font="Times 12");
lblKQ.pack(side=BOTTOM);


tk.mainloop();
