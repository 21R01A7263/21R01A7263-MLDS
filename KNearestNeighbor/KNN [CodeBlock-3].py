from sklearn.tree import DecisionTreeClassifier
svc = DecisionTreeClassifier()
svc.fit(X_train,y_train)
y_p=svc.predict(X_test)
print(accuracy_score(y_p,y_test))