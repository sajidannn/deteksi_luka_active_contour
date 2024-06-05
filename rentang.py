import numpy as np

# Data matriks satu dimensi yang diberikan
matriks = np.array([
    [70, 88, 210],
    [119, 118, 202],
    [65, 67, 168],
    [66, 83, 188]
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
