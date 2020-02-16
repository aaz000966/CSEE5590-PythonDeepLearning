import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# Correlation between Survived and Sex
train_df = pd.read_csv('./train.csv')
print(train_df[['Survived', 'Sex']].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False))

# mount the fire
train_df = pd.read_csv('./glass.csv')
X = train_df.drop("Type", axis=1)
Y = train_df["Type"]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.5, random_state=0)

# Nive Bayes constructor
gnb = GaussianNB()
Y_prediction = gnb.fit(X_train, y_train).predict(X_test)
acc_gnb = round(gnb.score(X_test, y_test) * 100, 2)
print("Naïve Bayes accuracy is:", acc_gnb)
print(classification_report(y_test, Y_prediction))

print("-" * 50)
# SVM (Code is given in class)
svc = SVC()
svc.fit(X_train, y_train)
y_pred = svc.predict(X_test)
acc_svc = round(svc.score(X_test, y_test) * 100, 2)
print("svm accuracy is:", acc_svc)

print(classification_report(y_test, y_pred))
