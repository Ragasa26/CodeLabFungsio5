import matplotlib.pyplot as plt
import numpy as np

#pastikan kalian sudah melakukan import library yang dibutuhkan
#sebelum menjalankan kode ini
xpoints = np.array([1, 8, 10])
ypoints = np.array([3, 10, 5])

plt.figure(figsize=(5,5))
plt.plot(xpoints, ypoints, color='red')

# Menambahkan label sumbu x dan y
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')

# Menambahkan judul plot
plt.title('Contoh Plot Garis')

plt.xlim([0,15])
plt.ylim([0,15])
plt.show()