import matplotlib.colors
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

excelFile = open("E_commerceCustomerBehavior_Sheet1.csv", "r")
excelData = pd.read_csv(excelFile)
# excelData2 = pandas.read_csv(excelFile)


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    '''print("Dataset Overview:")
    print(excelData.info())'''

    # Gender Distribution
    '''plt.figure(figsize=(10, 6))
    sns.countplot(x='Gender', data=excelData)
    plt.title('Gender Distribution')
    plt.show()'''
    # Age Distribution
    '''plt.figure(figsize=(10, 6))
    sns.histplot(excelData['Age'], bins=15, kde=True)
    plt.title('Age Distribution')
    plt.show()'''
    # Correlation Matrix
    numeric_columns = excelData.select_dtypes(include='number')
    correlation_matrix = numeric_columns.corr()

    # Data Exploration - Correlation Matrix (HeatMap)
    '''plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, annot_kws={"size":6}, fmt=".2f")
    plt.title('Correlation Matrix')
    plt.show()'''
    # Data Exploration - City Distribution
    '''plt.figure(figsize=(8, 6))
    sns.histplot(excelData['City'], bins=40)
    plt.title('City Distribution')
    plt.show()'''
    # Data Exploration - Average Rating
    '''plt.figure(figsize=(9, 7))
    sns.histplot(excelData['Average Rating'], bins=20, kde=True)
    plt.title('Average Rating')
    plt.show()'''
    # Data Exploration - Total Spend
    '''plt.figure(figsize=(9, 7))
    sns.kdeplot(data=excelData['Total Spend'])
    plt.title('Total Spend')
    plt.show()'''
    # Data Exploration - Items Purchased
    '''plt.figure(figsize=(9, 7))
    sns.histplot(data=excelData['Items Purchased'], color='Purple')
    plt.title('Items Purchased')
    plt.show()'''
    # Data Exploration - Days Since Last Purchase
    '''plt.figure(figsize=(9, 7))
    sns.histplot(excelData['Days Since Last Purchase'], color='orange')
    plt.title('Days Since Last Purchase')
    plt.show()'''
    '''# Data Exploration - Items Purchased
    plt.figure(figsize=(9, 7))
    sns.histplot(excelData['Items Purchased'], color='navy')
    plt.title('Items Purchased')
    plt.show()'''

    '''# visualize the gender && membership type
    gender_membership = excelData[['Gender', 'Membership Type']].value_counts().reset_index()
    sns.barplot(data=gender_membership, x='Gender', y='count', hue='Membership Type')
    plt.show()'''
    '''# find the relation between the average spending and gender
    gender_spend = excelData.groupby('Gender')['Total Spend'].mean()
    gender_spend.plot.bar()
    plt.title("Average Spending for each Gender")
    plt.show()'''

