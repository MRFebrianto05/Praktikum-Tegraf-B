# Data Soal
sequence = [4, 1, 13, 7, 0, 2, 8, 11, 3]

def find_longest_increasing_subsequence(arr):
    # Kita gunakan struktur Recursive dengan Memoization (supaya efisien)
    # Tapi karena soal meminta pendekatan Tree, kita simulasikan cara kerja tree
    
    # Fungsi untuk mencari kedalaman maksimal dari index tertentu
    def search_tree(current_index, current_val):
        # Cari anak-anak yang valid (index > current_index DAN value > current_val)
        possible_next_steps = []
        for i in range(current_index + 1, len(arr)):
            if arr[i] > current_val:
                # Rekursif: Lanjut cari ke dalam
                path_from_child = search_tree(i, arr[i])
                possible_next_steps.append(path_from_child)
        
        # Jika tidak ada langkah lagi (daun/leaf), kembalikan diri sendiri
        if not possible_next_steps:
            return [current_val]
        
        # Jika ada cabang, pilih cabang yang menghasilkan jalur TERPANJANG
        longest_subpath = max(possible_next_steps, key=len)
        return [current_val] + longest_subpath

    # Level 1: Coba mulai dari setiap angka di deret
    all_possible_paths = []
    for i in range(len(arr)):
        path = search_tree(i, arr[i])
        all_possible_paths.append(path)
    
    # Ambil pemenang (paling panjang)
    winner = max(all_possible_paths, key=len)
    return winner

# Eksekusi
solusi = find_longest_increasing_subsequence(sequence)
print(f"Data Awal: {sequence}")
print(f"Subsequence Terpanjang (LIS): {solusi}")
print(f"Panjang Langkah: {len(solusi)}")
