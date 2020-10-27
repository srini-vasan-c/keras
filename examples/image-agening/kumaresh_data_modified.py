# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 16:55:28 2020

@author: srinivasan.c
"""
#Inporting Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
from sklearn import cluster

#importing Dataset and seperating Dependent and independent Variables
dataset = pd.read_csv('data/im_data.csv')
x = dataset.iloc[:,1:4].values 
label_encoder = LabelEncoder()
dataset.iloc[:,4] = label_encoder.fit_transform(dataset.iloc[:,4]).astype('float64')
y = dataset.iloc[:,4].values

#Splitting training data and test Data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/4, random_state = 0)

#Defining Clusters
k = 4

#Defining KMeans Model using Train Data
kmeans = cluster.KMeans(n_clusters = k)
kmeans.fit(x_train)

#Predicting using Test Data
y_pred = kmeans.predict(x_test)

#Visualizing Predicted data using confusion matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)

#Hierchical Clustering
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters=4)
y_hcc = hc.fit(x_train,y_train)

y_hc = hc.fit_predict(x_test)
cm_h = confusion_matrix(y_test,y_hc)
print(cm_h)
plt.show()
plt.clf()
x=x_test
plt.scatter(x[y_hc == 0,0], x[y_hc == 0,1], c = 'red', label = 'Cluseter 1')
plt.scatter(x[y_hc == 1,0], x[y_hc == 1,1], c = 'blue',label = 'Cluseter 2')
plt.scatter(x[y_hc == 2,0], x[y_hc == 2,1], c = 'green',label = 'Cluseter 3')
plt.scatter(x[y_hc == 3,0], x[y_hc == 3,1], c = 'cyan',label = 'Cluseter 4')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1], c = 'yellow', s = 150, label = 'centeroid')
plt.title('HC Clustering')
plt.xlabel('Salary(k)')
plt.ylabel('Spent')
plt.legend()
plt.show()
#Graphical Visulization of Data
#Plot Code Starts
"""
from sklearn.decomposition import KernelPCA
pca = KernelPCA(n_components=2)
principalComponents = pca.fit_transform(x,y)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])

finalDf = pd.concat([principalDf, dataset[['CLASS']]], axis = 1)

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Component 1', fontsize = 15)
ax.set_ylabel('Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
targets = [0, 1, 2, 3]
colors = ['r', 'g', 'b', 'y']
for target, color in zip(targets,colors):
    indicesToKeep = finalDf['CLASS'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()

#Plot Code Ends
"""