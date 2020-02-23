import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

train = pd.read_csv('winequality-red.csv')

# handling missing value
data = train.select_dtypes(include=[np.number]).interpolate().dropna()

# Working with Numeric Features
numeric_features = train.select_dtypes(include=[np.number])

corr = numeric_features.corr()

print(corr['quality'].sort_values(ascending=False), '\n')
print(corr['quality'].sort_values(ascending=True))

print("Top features = alcohol, volatile acidity, and sulphates")

##Build a linear model
y = np.log(train.quality)
X = data.drop(['quality'], axis=1)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=42, test_size=.33)

from sklearn import linear_model

lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)
print("R^2 is: \n", model.score(X_test, y_test))
predictions = model.predict(X_test)
from sklearn.metrics import mean_squared_error

print('RMSE is: \n', mean_squared_error(y_test, predictions))

actual_values = y_test
plt.scatter(predictions, actual_values, alpha=.75,
            color='b')
plt.xlabel('Predicted Quality')
plt.ylabel('Actual Quality')
plt.title('Linear Regression Model')
plt.show()
