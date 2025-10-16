import socket
from datetime import datetime

# Konfigurasi server
SERVER_IP = "127.0.0.1"   # IP lokal (ubah jika perlu)
SERVER_PORT = 12345

# Buat socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

print(f"=== SERVER UDP AKTIF di {SERVER_IP}:{SERVER_PORT} ===\n")

# Jalankan server tanpa menutup koneksi
while True:
    # Terima data dari client
    data, addr = server_socket.recvfrom(1024)
    pesan = data.decode()

    # Catat waktu request
    waktu_request = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Tampilkan ke terminal
    print(f"[{waktu_request}] Pesan dari {addr}: {pesan}")

    # Simpan log ke file
    with open("log_server_udp.txt", "a") as log_file:
        log_file.write(f"[{waktu_request}] Dari {addr}: {pesan}\n")

    # Kirim balasan ke client
    balasan = f"Server menerima pesan: '{pesan}' pada {waktu_request}"
    server_socket.sendto(balasan.encode(), addr)
