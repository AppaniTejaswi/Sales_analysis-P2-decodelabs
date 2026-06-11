>>> import pandas as pd
>>> df = pd.read_csv(r"C:\Users\Tejaswi\Downloads\Dataset for Data Analytics - Sheet1.csv")
>>> print(df.shape)
(1200, 14)
>>> print(df.info())
<class 'pandas.DataFrame'>
RangeIndex: 1200 entries, 0 to 1199
Data columns (total 14 columns):
 #   Column           Non-Null Count  Dtype
---  ------           --------------  -----
 0   OrderID          1200 non-null   str
 1   Date             1200 non-null   str
 2   CustomerID       1200 non-null   str
 3   Product          1200 non-null   str
 4   Quantity         1200 non-null   int64
 5   UnitPrice        1200 non-null   float64
 6   ShippingAddress  1200 non-null   str
 7   PaymentMethod    1200 non-null   str
 8   OrderStatus      1200 non-null   str
 9   TrackingNumber   1200 non-null   str
 10  ItemsInCart      1200 non-null   int64
 11  CouponCode       891 non-null    str
 12  ReferralSource   1200 non-null   str
 13  TotalPrice       1200 non-null   float64
dtypes: float64(2), int64(2), str(10)
memory usage: 131.4 KB
None
>>> print(df.isnull().sum())
OrderID              0
Date                 0
CustomerID           0
Product              0
Quantity             0
UnitPrice            0
ShippingAddress      0
PaymentMethod        0
OrderStatus          0
TrackingNumber       0
ItemsInCart          0
CouponCode         309
ReferralSource       0
TotalPrice           0
dtype: int64
>>> print(df.describe())
          Quantity    UnitPrice  ItemsInCart   TotalPrice
count  1200.000000  1200.000000  1200.000000  1200.000000
mean      2.945833   356.412750     5.485000  1053.968300
std       1.407557   197.177146     2.281983   819.856558
min       1.000000    11.390000     1.000000    11.390000
25%       2.000000   186.062500     4.000000   410.520000
50%       3.000000   364.210000     5.000000   823.615000
75%       4.000000   521.570000     7.000000  1578.475000
max       5.000000   699.930000    10.000000  3456.400000
>>> print(df['Product'].value_counts())
Product
Printer    181
Tablet     179
Chair      178
Laptop     173
Desk       170
Monitor    163
Phone      156
Name: count, dtype: int64
>>> print(df['PaymentMethod'].value_counts())
PaymentMethod
Online         258
Cash           246
Credit Card    234
Debit Card     232
Gift Card      230
Name: count, dtype: int64
>>> print(df['ReferralSource'].value_counts())
ReferralSource
Instagram    259
Email        250
Google       241
Facebook     228
Referral     222
Name: count, dtype: int64
>>> print(df['TotalPrice'].sum())
1264761.96
>>> print(
...     df[
...         ['Quantity',
...          'UnitPrice',
...          'ItemsInCart',
...          'TotalPrice']
...     ].corr()
... )
             Quantity  UnitPrice  ItemsInCart  TotalPrice
Quantity     1.000000   0.014553     0.650061    0.615251
UnitPrice    0.014553   1.000000     0.000602    0.717081
ItemsInCart  0.650061   0.000602     1.000000    0.392540
TotalPrice   0.615251   0.717081     0.392540    1.000000
>>> import matplotlib.pyplot as plt
>>> df['OrderStatus'].value_counts().plot(kind='bar')
<Axes: xlabel='OrderStatus'>
>>> plt.title("Order Status")
Text(0.5, 1.0, 'Order Status')
>>> plt.show()
>>> df['PaymentMethod'].value_counts().plot(kind='bar')
<Axes: xlabel='PaymentMethod'>
>>> plt.title("Payment Method")
Text(0.5, 1.0, 'Payment Method')
>>> plt.show()
>>> df['ReferralSource'].value_counts().plot(kind='bar')
<Axes: xlabel='ReferralSource'>
>>> plt.title("Referral Source")
Text(0.5, 1.0, 'Referral Source')
>>> plt.show()
>>> df['TotalPrice'].hist()
<Axes: >
>>> plt.title("Distribution of Total Price")
Text(0.5, 1.0, 'Distribution of Total Price')
>>> plt.show()
>>> df.boxplot(column='TotalPrice')
<Axes: >
>>> plt.title("Boxplot of Total Price")
Text(0.5, 1.0, 'Boxplot of Total Price')
>>> plt.show()
>>> import seaborn as sns
>>> import matplotlib.pyplot as plt
>>> plt.figure(figsize=(8,6))
<Figure size 800x600 with 0 Axes>
>>> sns.heatmap(
...     df[['Quantity','UnitPrice','ItemsInCart','TotalPrice']].corr(),
...     annot=True,
...     cmap='coolwarm'
... )
<Axes: >
>>> plt.title('Correlation Heatmap')
Text(0.5, 1.0, 'Correlation Heatmap')
>>> plt.show()