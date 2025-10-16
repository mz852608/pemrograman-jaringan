import socket
from datetime import datetime

# Konfigurasi server tujuan
SERVER_IP = "127.0.0.1"  # Sama dengan server
SERVER_PORT = 12345

# Buat socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("=== CLIENT UDP ===")
print("Ketik 'exit' untuk keluar.\n")

# Loop kirim pesan ke server
while True:
    pesan = input("Masukkan pesan: ")

    if pesan.lower() == "exit":
        print("Client keluar...")
        break

    # Tambahkan timestamp di pesan
    waktu_kirim = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = f"[{waktu_kirim}] {pesan}"

    # Kirim pesan ke server
    client_socket.sendto(data.encode(), (SERVER_IP, SERVER_PORT))

    # Tunggu balasan dari server
    try:
        client_socket.settimeout(5)
        balasan, _ = client_socket.recvfrom(1024)
        print("Balasan server:", balasan.decode())
    except socket.timeout:
        print("Tidak ada balasan dari server (timeout).")

# Tutup socket setelah keluar
client_socket.close()
