X=df
y=iris['target']
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.33, random_state=42)
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski', metric_params=None, n_jobs=None, n_neighbors=3, p=2, weights='uniform')

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

y_pred=knn.predict(X_test)
cm=confusion_matrix(y_test, y_pred)
print(cm)
print("Correct prediction", accuracy_score(y_test, y_pred))
print("Wrong prediction", (1-accuracy_score(y_test,y_pred)))
y_testtrain=knn.predict(X_train)
cm1=confusion_matrix(y_train,y_testtrain)
print(cm1)
