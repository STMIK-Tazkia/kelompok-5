# Matriks C
C = np.array([
    [44, 55, 54, 10],
    [33, 5, 32, 13],
    [21, 7, 21, 11],
    [33, 88, 32, 15]
])

# Matriks D
D = np.array([
    [2, 1, 3, 1],
    [7, 1, 0, 7],
    [2, 0, 1, 2],
    [1, 3, 1, 2]
])

# Perkalian matriks C x D
result = np.dot(C, D)

# Menampilkan hasil
print("Hasil perkalian matriks C x D adalah:")
print(result)

# Definisi himpunan
A = {330, 50, 6, 4, 50, 18, 21, 3, 23, 133, 46, 77}
B = {122, 120, 1.56, 21, 210, 31, 50, 15, 6, 4, 337}

# Fungsi untuk menghitung irisan
def irisan(set1, set2):
    return set1.intersection(set2)

# Fungsi untuk menghitung beda setangkup
def beda_setangkup(set1, set2):
    return set1.symmetric_difference(set2)

# Fungsi untuk menghitung probabilitas
def probabilitas(set1, set2):
    union_set = set1.union(set2)
    return len(set1) / len(union_set), len(set2) / len(union_set)

# Menghitung hasil
hasil_irisan = irisan(A, B)
hasil_beda_setangkup = beda_setangkup(A, B)
prob_A, prob_B = probabilitas(A, B)

# Output hasil
print("Irisan A dan B:", hasil_irisan)
print("Beda setangkup A dan B:", hasil_beda_setangkup)
print("Probabilitas P(A):", prob_A)
print("Probabilitas P(B):", prob_B)
