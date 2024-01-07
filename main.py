import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('shoplist.csv')
print(df.head(5))

# Data 1

monthly_profit = df.groupby('month_number')['total_profits'].sum()

# Data 2

plt.figure(figsize=(10,6))
plt.plot(monthly_profit.index, monthly_profit.values, linestyle='-', color='blue', linewidth=2)
plt.xlabel('Monthly Number')
plt.ylabel('Total Profit')
plt.xlabel('Monthly Number')
plt.title('Total Profit for Each Month (Plain Line Plot)')
plt.grid(True)
plt.xticks(monthly_profit.index)
plt.show()


# Data 3

plt.figure(figsize=(10, 6))
plt.plot(monthly_profit.index, monthly_profit.values, linestyle='dotted', color='red', marker='o', markerfacecolor='red', markeredgecolor='purple', markersize=8, linewidth=3, label='Total Profit')
plt.xlabel('Month Number')
plt.ylabel('Sold Units Number')
plt.title('Company Sales data of last year')
plt.grid(True)
plt.legend(loc='lower right')
plt.xticks(monthly_profit.index)
plt.show()

# Data 4

products = df.drop(columns=['month_number', 'total_units', 'total_profits'])

plt.figure(figsize=(12, 6))
for product in products.columns:
    plt.plot(df['month_number'], df[product], marker='o', label=product)

plt.xlabel('Month Number')
plt.ylabel('Sold Units in Number')
plt.title('Sales data')
plt.grid(True)
plt.legend(loc='upper left')
plt.xticks(df['month_number'])
plt.show()


# Data 5
toothpaste_sales = df[['month_number', 'toothpaste']]

plt.figure(figsize=(10, 6))
plt.scatter(toothpaste_sales['month_number'], toothpaste_sales['toothpaste'], marker='o', color='cadetblue', label='Tooth paste sales data')
plt.xlabel('Month Number')
plt.ylabel('Number of units sold')
plt.title('Toothpaste Sales Data f')
plt.grid(True, linestyle='--')
plt.xticks(toothpaste_sales['month_number'])
plt.legend(loc='upper left', title_fontsize='large')
plt.show()

# Data 6

facecream_sales = df[['month_number', 'facecream']]
facewash_sales = df[['month_number', 'facewash']]

plt.figure(figsize=(10, 6))
bar_width = 0.4
plt.bar(facecream_sales['month_number'], facecream_sales['facecream'], width=bar_width, align='center', label='Face Cream', color='blue')
plt.bar(facewash_sales['month_number'] + bar_width, facewash_sales['facewash'], width=bar_width, align='center', label='Face Wash', color='orange')
plt.xlabel('Month Number')
plt.ylabel('Sales units in numbers')
plt.title('Face cream and Face Wash sales data')
plt.grid(True, linestyle='--')
plt.xticks(facecream_sales['month_number'] + bar_width / 2, facecream_sales['month_number'])
plt.legend(loc='upper left')
plt.show()


# Data 7

bathingsoap_sales = df[['month_number', 'bathingsoap']]

plt.figure(figsize=(10, 6))
plt.bar(bathingsoap_sales['month_number'], bathingsoap_sales['bathingsoap'], color='red')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title('Bathing Soap Sales Data')
plt.grid(True, linestyle='--')
plt.xticks(bathingsoap_sales['month_number'])
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.show()


# Data 8

monthly_profit = df.groupby('month_number')['total_profits'].sum()

plt.figure(figsize=(10, 6))
plt.hist(monthly_profit, bins=10, edgecolor='black', color='violet')
plt.xlabel('Profit Range in dollar')
plt.ylabel('Actual Profit in dollar')
plt.title('Profit Data')
plt.grid(True, linestyle='--')
plt.show()


# Data 9

last_year = df['month_number'].max() // 100

last_year_data = df[df['month_number'] // 100 == last_year]

total_sales_last_year = last_year_data.drop(columns=['month_number', 'total_units', 'total_profits']).sum()

plt.figure(figsize=(8, 8))
colors = ['red', 'lightcoral', 'lightskyblue', 'orange', 'pink', 'purple']
plt.pie(total_sales_last_year, labels=total_sales_last_year.index, autopct='%1.1f%%', colors=colors)
plt.title('Percentage of Units Sold per Product in Last Year')
plt.axis('equal')  
legend_labels = total_sales_last_year.index
plt.legend(legend_labels, title='Products', loc='lower right', bbox_to_anchor=(1.2, 0))
plt.show()


# Data 10

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

ax1.plot(df['month_number'], df['bathingsoap'], marker='o', color='red')
ax1.set_xlabel('Month Number')
ax1.set_ylabel('Sales units in number')
ax1.set_title('Sales Data of a Bathingsoap')

ax2.plot(df['month_number'], df['facewash'], marker='o', color='green')
ax2.set_xlabel('Month Number')
ax2.set_ylabel('sales Units in numbers')
ax2.set_title('Sales Data of a facewash')

plt.tight_layout()  
plt.show()

# Data 11

plt.figure(figsize=(10, 6))

months = df['month_number']
products = df.drop(columns=['month_number', 'total_units', 'total_profits'])
colors = ['gold', 'lightcoral', 'cadetblue', 'lightgreen', 'red', 'purple']

plt.stackplot(months, products.values.T, labels=products.columns, colors=colors)

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title('All Product Sales Data using Stack Plot')
plt.legend(loc='upper left')

plt.show()



