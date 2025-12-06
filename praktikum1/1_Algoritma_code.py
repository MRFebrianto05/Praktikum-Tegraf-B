# Ukuran Papan (8x8)
N = 8

# Gerakan Kuda (L-shape): (x, y)
moves = [
    (1, 2), (1, -2), (-1, 2), (-1, -2),
    (2, 1), (2, -1), (-2, 1), (-2, -1)
]

def is_valid(x, y, board):
    """Cek apakah langkah masih di dalam papan dan belum dikunjungi"""
    return 0 <= x < N and 0 <= y < N and board[y][x] == -1

def get_degree(x, y, board):
    """
    Heuristik Warnsdorff:
    Hitung ada berapa langkah selanjutnya yang mungkin dari posisi (x,y).
    Kita akan memprioritaskan kotak yang punya pilihan paling sedikit.
    """
    count = 0
    for dx, dy in moves:
        if is_valid(x + dx, y + dy, board):
            count += 1
    return count

def solve_knights_tour(start_x, start_y):
    # Inisialisasi papan dengan -1 (artinya belum dikunjungi)
    board = [[-1 for _ in range(N)] for _ in range(N)]
    
    # Kuda mulai di posisi awal (langkah ke-0)
    board[start_y][start_x] = 0
    
    # Simpan urutan koordinat untuk visualisasi nanti
    path = [(start_x, start_y)]
    
    # Mulai langkah dari 1 sampai 63
    curr_x, curr_y = start_x, start_y
    for step in range(1, N*N):
        # Cari semua langkah yang mungkin dari posisi sekarang
        possible_moves = []
        for dx, dy in moves:
            nx, ny = curr_x + dx, curr_y + dy
            if is_valid(nx, ny, board):
                # Hitung degree (prioritas) langkah tersebut
                priority = get_degree(nx, ny, board)
                possible_moves.append((priority, nx, ny))
        
        # Jika tidak ada langkah lagi tapi belum selesai, berarti gagal (buntu)
        if not possible_moves:
            return None 
        
        # Urutkan berdasarkan priority terendah (Warnsdorff's Rule)
        possible_moves.sort(key=lambda x: x[0])
        
        # Pilih langkah terbaik
        _, next_x, next_y = possible_moves[0]
        
        # Update papan dan posisi
        board[next_y][next_x] = step
        curr_x, curr_y = next_x, next_y
        path.append((curr_x, curr_y))
        
    return path

print("Fungsi Knight's Tour siap digunakan!")
