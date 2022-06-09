# https://pub.towardsai.net/logistic-regression-for-binary-classification-hands-on-with-scikit-learn-a5c06b0f2d60
'''

Table of contents:
1. Introduction
2. What type of problems can be solved with Logistic Regression
3. Mathematical Interpretation
4. The C parameter
5. Hands-On:
   -Import Libraries
   -Create Data
   -Exploratory data analysis
   -Splitting data into train and test data sets
   -Build and evaluate the model
   -Finding the best C value
   -Build a visualisation for the model
'''



#Import Libraries:
from random import random
from random import randint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from mlxtend.plotting import plot_decision_regions


#Fabricating variables:
#Creating values for FeNO with 3 classes:
FeNO_0 = np.random.normal(15,20, 100)
FeNO_1 = np.random.normal(35,20, 100)
FeNO_2 = np.random.normal(65, 20, 100)
#Creating values for FEV1 with 3 classes:
FEV1_0 = np.random.normal(4.50, 1, 100)
FEV1_1 = np.random.uniform(3.75, 1.2, 100)
FEV1_2 = np.random.uniform(2.35, 1.2, 100)
#Creating values for Broncho Dilation with 3 classes:
BD_0 = np.random.normal(150,49, 100)
BD_1 = np.random.uniform(250,50,100)
BD_2 = np.random.uniform(350, 50, 100)

#Creating labels variable with two classes (1)Disease (0)No disease:
not_asthma = np.zeros((150,), dtype=int)
asthma = np.ones((150,), dtype=int)

#Concatenate classes into one variable:
FeNO = np.concatenate([FeNO_0, FeNO_1, FeNO_2])
FEV1 = np.concatenate([FEV1_0, FEV1_1, FEV1_2])
BD = np.concatenate([BD_0, BD_1, BD_2])
dx = np.concatenate([not_asthma, asthma])

#Create DataFrame:
df = pd.DataFrame()
#Add variables to DataFrame:
df['FeNO'] = FeNO.tolist()
df['FEV1'] = FEV1.tolist()
df['BD'] = BD.tolist()
df['dx'] = dx.tolist()

#Exploring dataset:
sns.pairplot(df, kind="scatter", hue="dx")
plt.show()


sns.boxplot( x=df["dx"], y=df["FEV1"] )

sns.boxplot( x=df["dx"], y=df["FeNO"] )

sns.boxplot( x=df["dx"], y=df["BD"] )

sns.lmplot(x="FEV1", y="FeNO", data=df, fit_reg=True, hue='dx', legend=True)

sns.lmplot(x="FEV1", y="BD", data=df, fit_reg=True, hue='dx', legend=True)

sns.lmplot(x="FeNO", y="BD", data=df, fit_reg=True, hue='dx', legend=True)


#Creating X and y:
X = df.drop('dx', axis=1)
y = df['dx']
#Data split into train and test:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

#Fit the model:
logisticregression = LogisticRegression().fit(X_train, y_train)
#Evaluate the model:
print("training set score: %f" % logisticregression.score(X_train, y_train))print("test set score: %f" % logisticregression.score(X_test, y_test))


#C=100
logisticregression100 = LogisticRegression(C=100).fit(X_train, y_train)
print("training set score: %f" % logisticregression100.score(X_train, y_train))
print("test set score: %f" %
logisticregression100.score(X_test, y_test))

#C=0.01
logisticregression001 = LogisticRegression(C=0.01).fit(X_train, y_train)
print("training set score: %f" % logisticregression001.score(X_train, y_train))
print("test set score: %f" %
logisticregression001.score(X_test, y_test))

training_accuracy = []
test_accuracy = []
# try c values from 0.001 to 100:
c_settings = np.arange(0.001, 100, 0.1)
for i in c_settings:
    # build the model
    clf = LogisticRegression(C=i)
    clf.fit(X_train, y_train)
    # record training set accuracy
    training_accuracy.append(clf.score(X_train, y_train))
    # record generalization accuracy
    test_accuracy.append(clf.score(X_test, y_test))
plt.plot(c_settings, training_accuracy, label="training accuracy")
plt.plot(c_settings, test_accuracy, label="test accuracy")
plt.legend()

df.to_csv('data.csv', index = False)
data = pd.read_csv('data.csv')

def logisticReg_comparison(data,c):
    x = data[['FEV1','FeNO',]].values
    y = data['dx'].astype(int).values
    LogReg = LogisticRegression(C=c)
    LogReg.fit(x,y)
    print(LogReg.score(x,y))
    #Plot decision region:
    plot_decision_regions(x,y, clf=LogReg, legend=2)
    #Adding axes annotations:
    plt.xlabel('X_train')
    plt.ylabel('y_train')
    plt.title('LogReg with C='+str(c))
    plt.show()
logisticReg_comparison(data,12)