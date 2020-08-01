
from sklearn.svm import SVC
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
import cv2
import  numpy as np



def getData(path):
    trainingSet = pd.read_csv(path, nrows=20000)
    features = trainingSet.iloc[:, 1:]

    kichThuocAnh = (28,28)
    thuocTinhRutTrich = np.array([])

    # Rut trich dac trung anh
    for i in range(0,features.shape[0]):

        anhi = np.reshape( np.array(features.iloc[i,:]),kichThuocAnh ).astype("uint8");
        hog = cv2.HOGDescriptor(_winSize=(28, 28),
                                _blockSize=(8, 8),
                                _blockStride=(4, 4),
                                _cellSize=(4, 4),
                                _nbins=9);

        res =  np.array( hog.compute(anhi,None,None));
        res = res.reshape(1,res.shape[0]);
        thuocTinhRutTrich = np.append(thuocTinhRutTrich,res);

    labels = trainingSet.iloc[:, 0]

    return thuocTinhRutTrich, labels


def huanLuyen():


    features, labels = getData("mnist_train.csv")
    print("Load du lieu xong")
    print(features.shape);

    print("Tao Du lieu va model")
    featuresTrain, featuresTest, labelsTrain, labelsTest = train_test_split(features, labels, test_size=0.2,                                                                        random_state=20, stratify=labels)
    print(featuresTrain.shape)
    clf = SVC(kernel="rbf")

    print("bat dau huan luyen model. Vui long doi ...........")
    clf.fit(featuresTrain,labelsTrain)

    print("Chay qua trinh kiem thu........")
    predict= clf.predict(featuresTest)

    score = metrics.accuracy_score(labelsTest,predict)
    report =  metrics.classification_report(labelsTest,predict)

    print("Score: ",score)
    print(report)


    print ("Dang Luu Model .............")
    import joblib
    joblib.dump(clf,"mo-hinh-svm.joblib")
    print("Hoan thanh huan luyen model")
