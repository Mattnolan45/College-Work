import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

 
# read in files
df = pd.read_excel('MergedProj1.xlsx')


# drop unncessary colums 
X = df.drop(columns=['name','category','main_category','currency','deadline','state','country','launched'])

print(X.head())


# add in categorical data 

# main_Category

df['main_category'] = pd.Categorical(df['main_category'])

dfDummies = pd.get_dummies(df['main_category'], prefix = 'category')


X = pd.concat([X, dfDummies], axis=1)

#Category

df['category'] = pd.Categorical(df['category'])

dfDummies = pd.get_dummies(df['category'], prefix = 'category')


X = pd.concat([X, dfDummies], axis=1)


#Country

df['country'] = pd.Categorical(df['country'])

dfDummies = pd.get_dummies(df['country'], prefix = 'category')


X = pd.concat([X, dfDummies], axis=1)



# column to predict 
y = df['state'].values 

# split training data 
print("Split data\n")

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=1, stratify=y)

print("train data\n")
print("k = 10\n")
knn = KNeighborsClassifier(n_neighbors = 10)

# accuracy of whole dataset

knn.fit(X_train,y_train)

print("predict data\n")
print(knn.predict(X_test)[0:])

print("Accuracy\n")
print(knn.score(X_test, y_test))

## write something to find the difference between start and deadline.