import numpy as np
from sklearn.svm import SVC
import matplotlib.pyplot as plt

class MoHinhSVM:
    hangSo = 0;
    def __init__(self, iClassXanh,iClassDo,soC,kernel_ ):
        self.hangSo = soC;
        self.X1 = (iClassXanh) ;
        self.X2 = iClassDo;
        self.kernel = kernel_;
        self.huanLuyen();
        self.dungDoThi();


    def huanLuyen(self):
        Y1 = [];
        Y2 = [];
        for i in range(len(self.X1)):
            Y1.append(1);
        for i in range(len(self.X2)):
            Y2.append(-1);

        self.Y = np.array(Y1+Y2);
        self.X = np.vstack((self.X1,self.X2));
        hs = self.hangSo;
        self.classifition = SVC(kernel= self.kernel, C= hs);
        self.classifition.fit(self.X, self.Y);

    def dungDoThi(self):
         plt.plot(self.X1[:, 0], self.X1[:, 1], "bo", self.X2[:, 0], self.X2[:, 1], "ro");

         axe = plt.gca();
         xlim = axe.get_xlim()
         ylim = axe.get_ylim()

         x = np.linspace(xlim[0], xlim[1], 30)
         y = np.linspace(ylim[0], ylim[1], 30)
         Y, X = np.meshgrid(y, x)
         xy = np.vstack([X.ravel(), Y.ravel()]).T
         P = self.classifition.decision_function(xy).reshape(X.shape);
         axe.contour(X, Y, P, colors='green',
                     levels=[-1, 0, 1], alpha=0.5,
                     linestyles=['--', '-', '--']);
         plt.show();

# X1 = np.array( [[2,1],[2,4],[0,2]] );
# X2 =np.array( [[-1,4],[-2,3]] );
# X = np.vstack( (X1,X2) );
# Y = np.array([1,1,1,-1,-1]);
#
# classify = SVC(kernel = "linear" , C= 1);
# classify.fit(X,Y);
# axe = plt.gca();
# plt.plot(X1[:,0],X1[:,1], "go" ,X2[:,0],X2[:,1], "ro");
#
# xlim = axe.get_xlim()
# ylim = axe.get_ylim()
#
# x = np.linspace(xlim[0], xlim[1], 30)
# y = np.linspace(ylim[0], ylim[1], 30)
# Y, X = np.meshgrid(y, x)
# xy = np.vstack([X.ravel(), Y.ravel()]).T
# P = classify.decision_function(xy).reshape(X.shape);
# axe.contour(X, Y, P, colors='blue',
#            levels=[-1, 0, 1], alpha=0.5,
#            linestyles=['--', '-', '--']);
# plt.show();