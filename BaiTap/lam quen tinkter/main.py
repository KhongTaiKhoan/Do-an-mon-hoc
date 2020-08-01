from MyForm import ChuongTrinhThuNghiem
from svm import MoHinhSVM as mh
from tkinter import *
import tkinter.ttk as exTK
import numpy as np

# KHOI TAO CAC BIEN
iClass = 0; # 1 tuong truong cho class 1 va 2 tuong trung cho class 2
maMau = ["blue","red"];
iMangDo = list();
iMangXanh = list();
iMangXanh = list();
height = 500;
width = 800;
hangSoC = 1000;

demo = ChuongTrinhThuNghiem(width,height);
demo.title("Demo phân loại hai lớp");




#Chua cac ham xu ly
def Chon_Class():
    global  iClass;
    iClass = cbbClass.current();
    print(iClass);

def ThayDoiC():

    global hangSoC;
    hangSoC = int(etrC.get());
    print( hangSoC);

def Phan_Loai():

    moHinh = mh(np.array(iMangXanh),np.array(iMangDo),hangSoC, cbbKernel.get());


def Xoa():
    canvas.delete("all");
    iMangXanh.clear();
    iMangDo.clear();



# Tao khung ve
def taoDiem(event):
    x1,y1 = event.x-3,event.y-3;
    x2,y2 = event.x+3,event.y+3;
    canvas.create_rectangle(x1,y1,x2,y2,fill = maMau[iClass] ,outline = maMau[iClass]);
    if(iClass==0):
        iMangXanh.append([event.x,300-event.y]);
    else:
        iMangDo.append([event.x ,300- event.y ]);


width_canvas = 500;
canvas = Canvas(demo, width=width_canvas, bg = "white");
canvas.pack(fill = BOTH,side=LEFT);
canvas.bind("<Button-1>",taoDiem);

#Tao khung dieu khien
frame_root = Frame(demo)
frame_root.pack(fill=BOTH,side=LEFT);

frame = Frame(frame_root);
frame.pack(fill=X,side=TOP,pady=40);

  #--- CHINH SUA KHOANG CACH GIUA CAC ROW VA COLUMN
frame.columnconfigure(0, pad=3)
frame.columnconfigure(1, pad=3)
frame.columnconfigure(2, pad=10)

frame.rowconfigure(0, pad=10)
frame.rowconfigure(1, pad=10)
frame.rowconfigure(2, pad=10)
frame.rowconfigure(3, pad=10)



  #--- TAO INPUT NHAP SO C
Label(frame,text="Hằng C").grid(row=0,column=0);

etrC = Entry(frame,width = 15);
etrC.grid(row=0,column=1,sticky=W+E);
etrC.insert(0,"1000");

btnChonC = Button(frame,text="OK",command = ThayDoiC);
btnChonC.grid(row=0,column=2,sticky = W+E);

  #--- TAO COMBOBOX Chon Class
lblClass = Label(frame,text="Loại");
lblClass.grid(row=1,column=0);

cbbClass =  exTK.Combobox(frame);
cbbClass['value']=['Class 1','Class 2'];
cbbClass.current(0);
cbbClass.grid(row=1,column=1);

btnChonClass = Button(frame,text="OK", command = Chon_Class );
btnChonClass.grid(row=1,column=2,sticky = W+E);

   #---_ TAO loai kernel
lblKernel = Label(frame,text="Kernel");
lblKernel.grid(row=2,column=0,sticky=W);

cbbKernel =  exTK.Combobox(frame);
cbbKernel['value']=['linear','rbf'];
cbbKernel.current(0);
cbbKernel.grid(row=2,column=1,columnspan=2,sticky=W+E);

   #---_ TAO CAC BUTTON CONTROL

btnXoa = Button (frame,command = Xoa);
btnXoa.grid(columnspan=2,row=3,column=0, sticky=E);
btnXoa['text']="Xóa";

btnPL = Button (frame,command = Phan_Loai);
btnPL.grid(row=3,column=2,sticky=E);
btnPL['text']="Phân Loại";

demo.mainloop();


