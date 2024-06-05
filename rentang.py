import numpy as np

# Data matriks satu dimensi yang diberikan
matriks = np.array([
    [78, 96, 164],
    [56, 54, 172],
    [4, 8, 80],
    [37, 45, 98]
])

# Menghitung rentang untuk setiap komponen warna
min_values = np.min(matriks, axis=0)
max_values = np.max(matriks, axis=0)

print("Nilai minimum untuk setiap komponen warna:", min_values)
print("Nilai maksimum untuk setiap komponen warna:", max_values)

# Fungsi untuk memeriksa apakah matriks warna baru termasuk dalam rentang
def is_within_range(matriks_baru, min_vals, max_vals):
    return np.all((matriks_baru >= min_vals) & (matriks_baru <= max_vals))

# Contoh matriks warna baru
matriks_baru = np.array([80, 90, 200])

# Memeriksa apakah matriks warna baru termasuk dalam rentang
is_in_range = is_within_range(matriks_baru, min_values, max_values)
print("Apakah matriks baru termasuk dalam rentang warna luka abrasi?", is_in_range)
