import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
y3 = np.array([5, 9, 4, 12])  # Tambahkan array untuk garis ketiga

# Membuat plot untuk garis y1, y2, dan y3 dengan corak garis yang berbeda-beda
plt.plot(y1, label='Garis 1', color='blue', linestyle='-', marker='o')  # Garis biru, garis lurus, dan marker bulat
plt.plot(y2, label='Garis 2', color='green', linestyle='--', marker='s')  # Garis hijau, garis putus-putus, dan marker persegi
plt.plot(y3, label='Garis 3', color='red', linestyle=':', marker='^')  # Garis merah, garis titik-titik, dan marker segitiga

# Menambahkan judul dan label sumbu
plt.title('Plot Tiga Garis dengan Corak Berbeda')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

# Menambahkan keterangan (legend)
plt.legend()

plt.show()