import sklearn
import pandas as pd
from sklearn.datasets import load_iris
iris=load_iris()
print(iris.keys())
df=pd.DataFrame(iris['data'])
print(df)
print(iris['target_names'])
print(iris['feature_names'])
print(iris['target'])