import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder 


import numpy as np

df = pd.read_excel('MergedProj1.xlsx')


X = df.drop(columns=['name','category','main_category','currency','deadline','state','country','launched'])

print(X.head())

le = LabelEncoder()


y = df['state'].values # column to predict 

print("Split data\n")

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=1, stratify=y)

print("train data\n")
knn = KNeighborsClassifier(n_neighbors = 3)


# accuracy of whole dataset

knn.fit(X_train,y_train)

print("predict data\n")
print(knn.predict(X_test)[0:])

print("Accuracy\n")
print(knn.score(X_test, y_test))

