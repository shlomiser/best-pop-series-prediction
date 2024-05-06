import csv
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
from operator import itemgetter
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVC
import seaborn as sns
import numpy as np

filename = 'Data_Base.csv'
file_encoding = 'latin1'  # Replace with the appropriate encoding

df = pd.read_csv(filename, encoding=file_encoding)
print(df)

df = df.drop_duplicates()
df = df[df.iloc[:, 7] != '0']
df = df.reset_index(drop=True)
df.iloc[:, 7] = df.iloc[:, 7].str.split().str[0]
df.iloc[:, 7] = df.iloc[:, 7].str.split('$').str[1]
df.iloc[:, 7] = df.iloc[:, 7].str.replace(',', '')
df.iloc[:, 7] = df.iloc[:, 7].str.replace(' ', '')

print(df)



value_counts = df.iloc[:, 3].value_counts()
plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%')
plt.title('The Series that sales the most : ')
plt.axis('equal')
plt.show()

df[df.columns[7]] = df[df.columns[7]].astype(int)
sums_by_index3 = df.groupby(df.columns[3])[df.columns[7]].sum()
print(sums_by_index3)
df[df.columns[7]] = df[df.columns[7]].astype(int)
sums_by_index3 = df.groupby(df.columns[3])[df.columns[7]].sum()
sums_by_index3.plot(kind='bar')
plt.xlabel('Series')
plt.ylabel('Price')
plt.title('The Series whose sales brought the highest profit')
plt.show()

filtered_df = df[df[df.columns[3]] == 'Pop! Vinyl']
count_by_index7 = filtered_df.groupby(df.columns[7]).size()
count_by_index7.plot(kind='bar')
plt.xlabel('Price')
plt.ylabel('Count')
plt.title('The Price that come for the most of the Items in Pop! Vinyl :')
plt.show()

filtered_df = df[df[df.columns[3]] == 'Pop! Disney']
count_by_index7 = filtered_df.groupby(df.columns[7]).size()
count_by_index7.plot(kind='bar')
plt.xlabel('Price')
plt.ylabel('Count')
plt.title('The Price that come for the most of the Items in Pop! Disney :')
plt.show()

filtered_df = df[df[df.columns[3]] == 'Pop! Heroes']
count_by_index7 = filtered_df.groupby(df.columns[7]).size()
count_by_index7.plot(kind='bar')
plt.xlabel('Price')
plt.ylabel('Count')
plt.title('The Price that come for the most of the Items in Pop! Heroes :')
plt.show()

filtered_df = df[df[df.columns[3]] == 'Soda Figures']
count_by_index7 = filtered_df.groupby(df.columns[7]).size()
count_by_index7.plot(kind='bar')
plt.xlabel('Price')
plt.ylabel('Count')
plt.title('The Price that come for the most of the Items in Soda Figures :')
plt.show()


conditions = (df[df.columns[3]].isin(['Pop! Vinyl', 'Pop! Disney', 'Pop! Heroes', 'Soda Figures'])) & \
             (df[df.columns[5]].isin(['Chase', 'Exclusive', 'Limited Edition'])) & \
             (df[df.columns[6]].astype(float) >= 4.00) & \
             (df[df.columns[7]].astype(int) >= 20)
df['Y/N'] = conditions.apply(lambda x: 1 if x else 0)
print(df)

plt.title('The successful/unsuccessful Items graph : ')
print(df['Y/N'].value_counts())
plt.pie(df['Y/N'].value_counts(), labels=['0', '1'], autopct='%1.1f%%')
plt.show()


df.iloc[:, 5] = df.iloc[:, 5].str.replace('Exclusive', '2')
df.iloc[:, 5] = df.iloc[:, 5].str.replace('Chase', '1')
df.iloc[:, 5] = df.iloc[:, 5].str.replace('Limited Edition', '3')
df.iloc[:, 3] = df.iloc[:, 3].str.replace('Pop! Vinyl', '1')
df.iloc[:, 3] = df.iloc[:, 3].str.replace('Pop! Disney', '2')
df.iloc[:, 3] = df.iloc[:, 3].str.replace('Pop! Heroes', '3')
df.iloc[:, 3] = df.iloc[:, 3].str.replace('Soda Figures', '4')

#EDA:
group_0 = df[df['Y/N'] == 0]
group_1 = df[df['Y/N'] == 1]
print(group_0)
print(group_1)
group_0_data = group_0.iloc[:, 6]
group_1_data = group_1.iloc[:, 6]
x = ['unsuccessful group', 'successful group']
plt.bar(x[0], group_0_data.mean(), label='unsuccessful group')
plt.bar(x[1], group_1_data.mean(), label='successful group')
plt.xlabel('Ratings')
plt.ylabel('Amount')
plt.title('Average of ratings :')
plt.legend()
plt.show()


df2 = df.copy()
df2.drop(df2.columns[0], axis=1, inplace=True)
df2.drop(df2.columns[0], axis=1, inplace=True)
df2.drop(df2.columns[0], axis=1, inplace=True)
df2.drop(df2.columns[1], axis=1, inplace=True)
df2.drop(df2.columns[4], axis=1, inplace=True)
allowed_values = ['Pop! Vinyl', 'Pop! Disney', 'Pop! Heroes', 'Soda Figures']
df2.loc[~df2.iloc[:, 0].isin(allowed_values), df2.columns[0]] = 0
allowed_values = ['Chase', 'Exclusive', 'Limited Edition']
df2.loc[~df2.iloc[:, 1].isin(allowed_values), df2.columns[1]] = 0
print(df2)

X = df2
y = df['Y/N']

#LogisticRegression:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
LR_accuracy = accuracy_score(y_test, y_pred)
print("LogisticRegression Accuracy:", LR_accuracy)

#RandomForestRegressor
rf_regressor = RandomForestRegressor()
rf_regressor.fit(X_train, y_train)
y_pred = rf_regressor.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
RFR_accuracy = 1 - mse
print("RandomForestRegressor Accuracy:" , RFR_accuracy)

#svm:
svm_classifier = SVC()
svm_classifier.fit(X_train, y_train)
y_pred = svm_classifier.predict(X_test)
SVM_accuracy = accuracy_score(y_test, y_pred)
print("SVM Accuracy:", SVM_accuracy)

accuracies = [LR_accuracy, RFR_accuracy, SVM_accuracy]
models = ['Logistic Regression', 'SVM', 'Random Forest']
plt.pie(accuracies, labels=models, autopct='%1.1f%%')
plt.title('Accuracy Comparison')
plt.show()

df.describe()
