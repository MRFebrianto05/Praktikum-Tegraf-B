# Tugas Praktikum Teori Graf
Repositori ini berisi implementasi algoritma untuk menyelesaikan dua masalah Teori Graf: **The Knight's Tour (Perjalanan Kuda)** dan **Largest Monotonically Increasing Subsequence (LIS) menggunakan representasi Tree**.

## Persyaratan Sistem
Program ditulis dalam **Python 3** menggunakan format Jupyter Notebook (`.ipynb`). Library yang dibutuhkan:
  - `networkx` (untuk manipulasi graf)
  - `matplotlib` (untuk visualisasi/menggambar)
Instalasi library:
```
pip install networkx matplotlib
```

## 1. Program Knight's Tour
Menyelesaikan masalah langkah kuda catur pada papan 8x8 agar mengunjungi setiap petak tepat satu kali menggunakan **Heuristik Warnsdorff**.

### Cara Penggunaan
1. Buka file notebook (misal: `Praktikum1.ipynb`).
2. Jalankan cell `Algoritma Code` dan `Visualisasi Code`.
3. Pada cell eksekusi (paling bawah), tentukan koordinat awal kuda.
4. Jalankan cell tersebut untuk melihat hasil.

### Input
Variabel pada kode utama:
- `start_x`: Koordinat X posisi awal (integer 0 - 7).
- `start_y`: Koordinat Y posisi awal (integer 0 - 7).

### Output
- **Teks**: Status keberhasilan, jumlah langkah, dan tipe tur (Open Tour atau Closed Tour).
- **Visualisasi**: Gambar papan catur 8x8 dengan garis yang menunjukkan urutan perjalanan kuda dari Start (Hijau) ke End (Merah).

## 2. Program LIS (Largest Monotonically Increasing Subsequence) Tree
Mencari sub-urutan angka menaik terpanjang dengan memodelkan semua kemungkinan langkah sebagai struktur **Pohon (Tree)**.

### Cara Penggunaan
1. Buka file notebook (misal: `Praktikum2.ipynb`).
2. Cari variabel `sequence` di bagian atas kode.
3. Masukkan deret angka soal ke dalam list tersebut.
4. Jalankan semua cell.

### Input
- sequence: List berisi deret bilangan bulat.
  - Contoh: [4, 1, 13, 7, 0, 2, 8, 11, 3]

### Output
- **Teks**: Menampilkan deret LIS terpanjang yang ditemukan beserta panjangnya.
- **Visualisasi**: Gambar graf berstruktur Pohon (Tree) yang menunjukkan semua kemungkinan cabang keputusan yang valid (angka anak > angka induk). Graf disusun secara hirarkis dari atas ke bawah.
