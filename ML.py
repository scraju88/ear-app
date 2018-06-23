# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 07:17:37 2018

@author: SCRAJU88
"""

import numpy as np
import os
import glob
from random import shuffle

from sklearn import preprocessing, model_selection, svm, neighbors, metrics
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectPercentile, f_classif




os.chdir('C:/Users/SCRAJU88/Documents/Main Docs/Life Stuff/Product Ideas/Pediabyte/Smartphone Reflectometry/Data/Test Data/Machine Learning Dat Files/');


features = sorted(glob.glob('*features.dat'))
diagnosis = sorted(glob.glob('*diagnosis.dat'))
diagnosis2= sorted(glob.glob('*diagnosis2.dat'))


ftemparray = np.zeros(shape=(1,2600))


for f in features:
    ftemp = np.genfromtxt(fname=f, dtype="float")
    ftemparray = np.concatenate((ftemparray,ftemp),axis=0)

farray = np.delete(ftemparray, 0, axis=0) #axis zero is horizontal (i.e. x axis)

darray = [ ]

for d in diagnosis:
    dtemp = np.genfromtxt(fname=d, dtype="float")
    darray = np.concatenate((darray,dtemp),axis=0)

f_train, f_test, d_train, d_test = train_test_split(farray,darray,test_size=0.5)

model = svm.SVC(kernel='linear')
model.fit(f_train, d_train)

accuracy = model.score(f_test, d_test)


earray = [ ]

for e in diagnosis2:
    etemp = np.genfromtxt(fname=e, dtype="float")
    earray = np.concatenate((earray,etemp),axis=0)


atemparray = np.zeros(shape=(1,2600))
barray = [ ]

counter = -1

for a in farray:
    counter += 1 
    if model.predict(farray[counter:counter+1]) != 0 or earray[counter:counter+1] != 0:
        atemparray = np.concatenate((atemparray,farray[counter:counter+1]),axis=0)
        barray = np.concatenate((barray,earray[counter:counter+1]))


aarray = np.delete(atemparray, 0, axis=0) #axis zero is horizontal (i.e. x axis)

a_train, a_test, b_train, b_test = train_test_split(aarray,barray,test_size=0.5)

clf = svm.SVC(kernel='linear')
clf.fit(a_train, b_train)

accuracy2 = clf.score(a_test, b_test)

expected = b_test
predicted = clf.predict(a_test)

print(accuracy) 
print(accuracy2)

print("Classification report for classifier %s:\n%s\n"
      % (clf, metrics.classification_report(expected, predicted)))
 
print(clf, metrics.confusion_matrix(expected, predicted))

fpr, tpr, thresholds = metrics.roc_curve(expected, predicted, pos_label=2)
print(metrics.auc(fpr,tpr))

X_indices = np.arange(aarray.shape[-1])

selector = SelectPercentile(f_classif, percentile=10)
selector.fit(aarray, barray)
scores = -np.log10(selector.pvalues_)
scores /= scores.max()
plt.bar(X_indices - .45, scores, width=.2,
        label=r'Univariate score ($-Log(p_{value})$)', color='g')




# =============================================================================
# X = farray 
# y = darray
# 
# 
# 
# 
# n_features = X.shape[1]
# 
# C = 1.0
# kernel = 1.0 * RBF([1.0, 1.0])  # for GPC
# 
# # Create different classifiers. The logistic regression cannot do
# # multiclass out of the box.
# classifiers = {'L1 logistic': LogisticRegression(C=C, penalty='l1'),
#                'L2 logistic (OvR)': LogisticRegression(C=C, penalty='l2'),
#                'Linear SVC': SVC(kernel='linear', C=C, probability=True,
#                                  random_state=0),
#                'L2 logistic (Multinomial)': LogisticRegression(
#                 C=C, solver='lbfgs', multi_class='multinomial')
#                }
# 
# n_classifiers = len(classifiers)
# 
# # =============================================================================
# # plt.figure(figsize=(3 * 2, n_classifiers * 2))
# # plt.subplots_adjust(bottom=.2, top=.95)
# # 
# # =============================================================================
# xx = np.linspace(3, 9, 100)
# yy = np.linspace(1, 5, 100).T
# xx, yy = np.meshgrid(xx, yy)
# Xfull = np.c_[xx.ravel(), yy.ravel()]
# 
# for index, (name, classifier) in enumerate(classifiers.items()):
#     classifier.fit(X, y)
# 
#     y_pred = classifier.predict(X)
#     classif_rate = np.mean(y_pred.ravel() == y.ravel()) * 100
#     print("classif_rate for %s : %f " % (name, classif_rate))
# 
# # =============================================================================
# #     # View probabilities=
# #     probas = classifier.predict_proba(Xfull)
# #     n_classes = np.unique(y_pred).size
# #     for k in range(n_classes):
# #         plt.subplot(n_classifiers, n_classes, index * n_classes + k + 1)
# #         plt.title("Class %d" % k)
# #         if k == 0:
# #             plt.ylabel(name)
# #         imshow_handle = plt.imshow(probas[:, k].reshape((100, 100)),
# #                                    extent=(3, 9, 1, 5), origin='lower')
# #         plt.xticks(())
# #         plt.yticks(())
# #         idx = (y_pred == k)
# #         if idx.any():
# #             plt.scatter(X[idx, 0], X[idx, 1], marker='o', c='k')
# # 
# # ax = plt.axes([0.15, 0.04, 0.7, 0.05])
# # plt.title("Probability")
# # plt.colorbar(imshow_handle, cax=ax, orientation='horizontal')
# # 
# # plt.show()
# # 
# # =============================================================================
# 
# 
# =============================================================================
