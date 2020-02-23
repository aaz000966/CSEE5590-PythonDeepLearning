import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
train = pd.read_csv('train.csv')
garage_df = train.get('GarageArea')

plt.scatter(train.get('GarageArea'), train.get('SalePrice'), color='b')
plt.ylabel('Sale Price')
plt.xlabel('Garage Area')
plt.title('OLD')
plt.show()

zScore = np.abs(stats.zscore(garage_df))
print(zScore)
print("_"*40)
outliers = []
ToBeDropped = []

for i, score in enumerate(zScore):
    if score > 2:
        outliers.append((i, score))
        ToBeDropped.append(i)
        print(i, score)
print(outliers)
print("_"*40)

train.drop(train.index[ToBeDropped], inplace=True)

plt.scatter(train.get('GarageArea'), train.get('SalePrice'), color='b')
plt.ylabel('Sale Price')
plt.xlabel('Garage Area')
plt.title('New')
plt.show()

