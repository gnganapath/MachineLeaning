#Data Preprocessing

#importing libraraties
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import dataset
dataset = pd.read_csv("Data_preprocessing.csv")
dataset.isnull().sum()

#dependent and independent variable
x = dataset.iloc[:,0:3].values
y = dataset.iloc[:,3:4]

#import imputer and fill the null values
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = "NAN", strategy = "mean", axis = 0)
Imputer = imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1,3])