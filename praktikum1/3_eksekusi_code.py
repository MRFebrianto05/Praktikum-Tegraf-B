# Tentukan posisi awal (0-7). Misal mulai di pojok kiri bawah (0,0)
start_x = 0
start_y = 7

# Cari Jalur
jalur = solve_knights_tour(start_x, start_y)

if jalur:
    print(f"Sukses! Ditemukan jalur dengan {len(jalur)} langkah.")
    
    # Cek apakah Open atau Closed Tour
    sx, sy = jalur[0]
    ex, ey = jalur[-1]
    
    # Cek apakah titik akhir bisa menyerang titik awal
    is_closed = False
    for dx, dy in moves:
        if ex + dx == sx and ey + dy == sy:
            is_closed = True
            break
            
    status = "Closed Tour (Sirkuit)" if is_closed else "Open Tour (Lintasan)"
    print(f"Tipe: {status}")
    
    # Gambar hasilnya
    draw_tour(jalur, title=f"Knight's Tour 8x8 - {status}")
else:
    print("Maaf, gagal menemukan jalur dari titik start ini.")
