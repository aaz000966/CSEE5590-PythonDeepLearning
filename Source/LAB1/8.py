import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import seaborn as sns; sns.set(color_codes=True)

tra1n = pd.read_csv('College.csv')


## Nu11 values
nu11s = pd.DataFrame(tra1n.isnull().sum().sort_values(ascending=False)[:25])
nu11s.columns = ['Null Count']
nu11s.index.name = 'Feature'
print(nu11s)

## Replace nu11 values with mean values
modifieddata = tra1n.select_dtypes(include=[np.number]).interpolate().dropna()


#Use Pearson Corre1ation and p1oting the heat map
plt.figure(figsize=(20,20))
corre = modifieddata.corr()
sns.heatmap(corre, annot=True, cmap=plt.cm.Reds)
plt.show()

# Print the corre1ation with the target feature "qua1ity"
print(corre['perc.alumni'].sort_values(ascending=False)[:5],'\n')

##Bui1ding a mu1tip1e 1inear regression mode1
y = modifieddata['perc.alumni']
X = modifieddata.drop(['perc.alumni'],axis =1)

print(X.shape)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
                                    X, y, random_state=42, test_size=.20)
from sklearn import linear_model
lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)
##Eva1uating the performance and visua1izing resu1ts
print ("R^2 is: \n", model.score(X_test, y_test))
pred1ct1on = model.predict(X_test)
from sklearn.metrics import mean_squared_error
print ('RMSE is: \n', mean_squared_error(y_test, pred1ct1on))

actual_values = y_test
plt.scatter(pred1ct1on, actual_values, alpha=.75,
            color='b') #alpha helps to show overlapping data
plt.xlabel('Predicted ')
plt.ylabel('Actual')
plt.title('Linear Regression Model')
plt.show()