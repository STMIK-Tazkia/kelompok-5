# Fungsi untuk menghitung perkalian matriks
def multiply_matrices(C, D):
    # Inisialisasi matriks hasil dengan ukuran 4x4
    result = [[0 for _ in range(4)] for _ in range(4)]
    
    # Proses perkalian matriks
    for i in range(4):
        for j in range(4):
            for k in range(4):
                result[i][j] += C[i][k] * D[k][j]
    return result

# Matriks C
C = [
    [44, 55, 54, 10],
    [33, 5, 32, 13],
    [21, 7, 21, 11],
    [33, 88, 32, 15]
]

# Matriks D
D = [
    [2, 1, 3, 1],
    [7, 2, 0, 1],
    [2, 0, 1, 2],
    [1, 3, 1, 2]
]

# Hitung hasil perkalian matriks
result = multiply_matrices(C, D)

# Cetak hasilnya
print("Hasil perkalian matriks C x D:")
for row in result:
    print(row)