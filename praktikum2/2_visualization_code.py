import networkx as nx
import matplotlib.pyplot as plt

# Data Soal
sequence = [4, 1, 13, 7, 0, 2, 8, 11, 3]

# Membuat Graf Berarah
G = nx.DiGraph()
labels = {}
node_id_counter = 0

# --- FUNGSI PEMBANGUN POHON YANG DIPERBAIKI ---
# Kita tambahkan parameter 'level' untuk mencatat kedalaman node
def build_visual_tree_layered(parent_id, current_idx, current_val, level):
    global node_id_counter
    
    for i in range(current_idx + 1, len(sequence)):
        if sequence[i] > current_val:
            node_id_counter += 1
            my_id = node_id_counter
            
            # Tambahkan Node dengan atribut 'layer'
            # Semakin dalam levelnya, semakin ke bawah posisinya nanti
            G.add_node(my_id, layer=level)
            G.add_edge(parent_id, my_id)
            labels[my_id] = sequence[i]
            
            # Rekursif ke level berikutnya
            build_visual_tree_layered(my_id, i, sequence[i], level + 1)

# Setup Root (Titik Awal) di layer 0
root_id = 0
G.add_node(root_id, layer=0)
labels[root_id] = "Start"

# Jalankan fungsi pembangun mulai dari level 1
build_visual_tree_layered(root_id, -1, -1, 1)

# --- BAGIAN MENGGAMBAR YANG DIPERBAIKI ---
plt.figure(figsize=(14, 10)) # Ukuran gambar diperbesar

# --- KUNCI PERBAIKAN: Gunakan Multipartite Layout ---
# Layout ini akan menyusun node berdasarkan atribut 'layer' yang kita buat tadi
pos = nx.multipartite_layout(G, subset_key='layer', align='horizontal')

# Gambar Node, Edge, dan Label
# Kita perkecil sedikit node dan font agar muat banyak
nx.draw_networkx_nodes(G, pos, node_size=600, node_color='white', edgecolors='black')
nx.draw_networkx_edges(G, pos, edge_color='#1f1f1f', arrows=True, arrowstyle='-|>', node_size=600)
nx.draw_networkx_labels(G, pos, labels=labels, font_size=9)

plt.title("Visualisasi Pohon LIS (Layered Layout)", fontsize=16)
# Membalik sumbu Y agar Start ada di atas dan pohon tumbuh ke bawah
plt.gca().invert_yaxis()
plt.axis('off')
plt.show()
