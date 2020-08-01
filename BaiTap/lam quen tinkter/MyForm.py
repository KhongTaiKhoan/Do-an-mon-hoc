from tkinter import *

class ChuongTrinhThuNghiem (Tk):
    def __init__(self,sizeX, sizeY):
        Tk.__init__(self);
        self.sizeX = sizeX;
        self.sizeY = sizeY;
        screenHeight = self.winfo_screenheight();
        screenWidth = self.winfo_screenwidth();
        posX = screenWidth / 2 - self.sizeX / 2;
        posY = screenHeight / 2 - self.sizeY / 2;
        self.geometry("%dx%d+%d+%d" % (self.sizeX, self.sizeY, posX, posY));
        self.initUI();
    def initUI (self):
        frame = Frame(self);
        frame.pack(fill=X);


