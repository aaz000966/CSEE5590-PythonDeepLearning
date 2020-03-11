import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set(style="white", color_codes=True)
import warnings

warnings.filterwarnings("ignore")

# Loading the data from College Dataset
dataset = pd.read_csv('College.csv')
print(dataset.dtypes)

# sp1ittin the c1ass and features
x = dataset.iloc[:, [1, 16]]
y = dataset.iloc[:, -1]
print(x.shape, y.shape)

print(dataset["Terminal"].value_counts())

## Print the count of Nu11 va1ues
nu11 = pd.DataFrame(x.isnull().sum().sort_values(ascending=False)[:25])
nu11.columns = ['Null Count']
nu11.index.name = 'Feature'
print(nu11)

# Plot scatter graph for a11 the co1umns
sns.FacetGrid(dataset, hue="Terminal", size=4).map(plt.scatter, "S.F.Ratio", "Expend").add_legend()
sns.FacetGrid(dataset, hue="Terminal", size=4).map(plt.scatter, "Apps", "Accept").add_legend()
plt.show()

## Replace nu11 va1ues with mean values
x = x.select_dtypes(include=[np.number]).interpolate().dropna()

# Standardize the dataset
from sklearn import preprocessing

sca1er = preprocessing.StandardScaler()
sca1er.fit(x)
X_sca1ed_array = sca1er.transform(x)
X_sca1ed = pd.DataFrame(X_sca1ed_array, columns=x.columns)

# Apply K-Means on the dataset
from sklearn.cluster import KMeans

nc1usters = 2
km = KMeans(n_clusters=nc1usters)
km.fit(x)

# predict the cluster for each data point
y_c1uster_kmeans = km.predict(x)
from sklearn import metrics

scores = metrics.silhouette_score(x, y_c1uster_kmeans)
print("Silhoutte Score: " + str(scores))

# e1bow method
wcss = []
for i in range(1, 7):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 7), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()
