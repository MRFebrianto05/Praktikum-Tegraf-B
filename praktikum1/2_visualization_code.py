import matplotlib.pyplot as plt

def draw_tour(path, title="Knight's Tour"):
    plt.figure(figsize=(8, 8))
    ax = plt.gca()
    
    # 1. Gambar Papan Catur
    for x in range(N):
        for y in range(N):
            # Warna selang-seling (putih & abu-abu)
            color = 'white' if (x + y) % 2 == 0 else 'lightgray'
            rect = plt.Rectangle((x, y), 1, 1, facecolor=color)
            ax.add_patch(rect)
            
    # 2. Gambar Jalur Kuda
    # Pisahkan koordinat X dan Y dari path
    x_coords = [p[0] + 0.5 for p in path] # +0.5 agar titiknya di tengah kotak
    y_coords = [p[1] + 0.5 for p in path]
    
    # Gambar garis penghubung (Route)
    plt.plot(x_coords, y_coords, color='black', linewidth=1.5, marker='o', markersize=5)
    
    # Tandai Awal (Hijau) dan Akhir (Merah)
    plt.plot(x_coords[0], y_coords[0], 'go', markersize=15, label='Start') # Start
    plt.plot(x_coords[-1], y_coords[-1], 'ro', markersize=15, label='End') # End
    
    # Panah arah (opsional, agar terlihat alurnya)
    # Kita gambar panah di beberapa titik saja agar tidak semrawut
    for i in range(0, len(path)-1, 1):
        plt.arrow(x_coords[i], y_coords[i], 
                  (x_coords[i+1]-x_coords[i])*0.5, (y_coords[i+1]-y_coords[i])*0.5, 
                  head_width=0.1, color='black')

    # Setting Tampilan
    plt.xlim(0, N)
    plt.ylim(0, N)
    plt.xticks(range(N))
    plt.yticks(range(N))
    plt.grid(True, color='black', linewidth=0.5)
    plt.title(title, fontsize=15)
    plt.legend()
    plt.axis('off') # Matikan axis angka jika ingin bersih
    plt.show()

print("Fungsi Visualisasi siap!")
