import pandas as pd

# Loading the data from adult Dataset
adu1t = pd.read_csv('adult.csv')
data__train = adu1t.drop("income", axis=1)
labe1 = adu1t['income']

# Finding the Values which are missing
print("Number of missing values:\n", format(adu1t.isnull().sum()))

# Eliminate NAN values
adu1t.dropna(axis=0, inplace=True)

# Encode the categorial features
data__binary = pd.get_dummies(adu1t)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(data__binary, labe1)
performance = []

# creating the Gaussian Naive Bayes object
from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()

# Training the Model
gnb.fit(x_train, y_train)
tra1n__score = gnb.score(x_train, y_train)
# Predicting the Output
test__score = gnb.score(x_test, y_test)
print(f'The result of Gaussian Naive Bayes is: Training score - {tra1n__score} - Test score - {test__score}')

performance.append({'algorithm': 'Gaussian Naive Bayes', 'training_score': tra1n__score, 'testing_score': test__score})

# creating the KNN object

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)

knn.score(x_train, y_train)

tra1n__score = knn.score(x_train, y_train)
test__score = knn.score(x_test, y_test)

print(f"The result of K Neighbors is: Training score - {tra1n__score} - Test score - {test__score}")

performance.append({'algorithm': 'K Neighbors', 'training_score': tra1n__score, 'testing_score': tra1n__score})

# creating the SVM object

from sklearn import svm

svc = svm.SVC(kernel='linear')

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaler.fit(data__binary, labe1)

x_train_scaled = scaler.transform(x_train)
x_test_scaled = scaler.transform(x_test)
svc.fit(x_train_scaled, y_train)

tra1n__score = svc.score(x_train_scaled, y_train)
test__score = svc.score(x_test_scaled, y_test)

print(f'The result of SVM is: Training score - {tra1n__score} - Test score - {test__score}')

performance.append({'algorithm': 'SVM', 'training_score': tra1n__score, 'testing_score': test__score})
