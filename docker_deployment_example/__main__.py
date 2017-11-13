import pandas as pd
from . import transformations
from sklearn.externals import joblib
from sklearn.linear_model import LinearRegression


data = pd.read_csv('data/stackloss.csv')
data = transformations.apply(data)

X = data.drop("target", axis=1)
y = data["target"]

model = LinearRegression()
model.fit(X,y)

joblib.dump(model, 'build/model')