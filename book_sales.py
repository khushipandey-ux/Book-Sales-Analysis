# -*- coding: utf-8 -*-
"""Book Sales.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FuUd2H_eHP6kNxYQTF36XAWyxlf1sbbB
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('Books_Data_Clean.csv')

df.head(4)

df.describe()

df=df[df['Publishing Year']>1990]

df.isna().sum()

df.dropna(subset='Book Name',inplace=True)

df.duplicated().sum()

df.nunique()

plt.hist(df['Publishing Year'])
plt.xlabel('Publishing Year')
plt.ylabel('Frequency')
plt.title('Distribution of Publishing Year')
plt.show()

df['genre'].value_counts().plot(kind='bar')
plt.xlabel('Genre')
plt.ylabel('Frequency')
plt.title('Distribution of Genre')
plt.show()

df.groupby('Author')['Book_average_rating'].mean()

sns.boxplot(x='genre',y='Book_ratings_count',data=df)
plt.xlabel('Genre')
plt.ylabel('Book Ratings Count')
plt.title('Boxplot Distribution of Book Ratings Count by Genre')
plt.show()

plt.scatter(df['sale price'],df['units sold'])
plt.xlabel('Sale Price')
plt.ylabel('Units Sold')
plt.title('Scatter Plot of Sale Price vs Units Sold')
plt.show()

language_counts = df['language_code'].value_counts()

plt.pie(language_counts, labels=language_counts.index,startangle=90,autopct='%1.1f%%')
plt.title('Language Distribution of Books')
plt.show()

df.columns

df.groupby('Publisher ')['publisher revenue'].sum().sort_values(ascending=False)

df.groupby('Author_Rating')['Book_ratings_count'].mean().sort_values(ascending=False)

df.groupby('language_code').size().sort_values(ascending=False)

df.groupby('Author_Rating')['Book_ratings_count'].var()

plt.scatter(df['Book_average_rating'],df['Book_ratings_count'])
plt.xlabel('Book Average Rating')
plt.ylabel('Book Ratings Count')
plt.title('Scatter Plot of Book Average Rating vs Book Ratings Count')
plt.show()

total_gross_sales_author=df.groupby('Author')['gross sales'].sum()

total_gross_sales_author.sort_values(ascending=False).head(20).plot(kind='bar')
plt.xlabel('Author')
plt.ylabel('Total Gross Sales')
plt.title('Total Gross Sale for Each author')
plt.show()

sns.boxplot(x='Author_Rating' ,y='units sold',data=df)
plt.xlabel('Author_Rating')
plt.ylabel('Units Sold')
plt.title('Boxplot Distribution of Units Sold by Author_Rating')
plt.show()

df.groupby('Publishing Year')['units sold'].sum().plot(kind='line', marker='o')
plt.xlabel('Publishing Year')
plt.ylabel('Total Units Sold')
plt.title('Total Units Sold by Publishing Year')
plt.show()