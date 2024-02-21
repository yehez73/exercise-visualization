import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('nsp\sales_data.csv')

print("Data Penjualan:")
print(data)

total_sales = np.sum(data['Sales'])
average_sales = np.mean(data['Sales'])
max_sales = np.max(data['Sales'])
min_sales = np.min(data['Sales'])

print("\nTotal penjualan:", total_sales)
print("Rata-rata penjualan:", average_sales)
print("Penjualan tertinggi:", max_sales)
print("Penjualan terendah:", min_sales)

plt.figure(figsize=(10, 6))
sns.barplot(x='Store', y='Sales', data=data, palette='viridis')
plt.xlabel('Toko')
plt.ylabel('Penjualan')
plt.title('Penjualan per Toko')
plt.grid(True)
plt.show()