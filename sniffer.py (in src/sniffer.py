import socket
import struct
import binascii

def eth_frame(data):
    dest_mac, src_mac, proto = struct.unpack('!6s6sH', data[:14])
    return binascii.hexlify(dest_mac), binascii.hexlify(src_mac), socket.htons(proto), data[14:]

def ipv4_packet(data):
    version_header_length = data[0]
    header_length = (version_header_length & 15) * 4
    src = socket.inet_ntoa(data[12:16])
    dest = socket.inet_ntoa(data[16:20])
    proto = data[9]
    return src, dest, proto, data[header_length:]

def main():
    try:
        # For Linux: use AF_PACKET
        conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
        print("[*] Packet sniffer started...\n")
    except PermissionError:
        print("[!] Permission denied. Run as administrator/root.")
        return

    while True:
        raw_data, addr = conn.recvfrom(65536)
        dest_mac, src_mac, eth_proto, data = eth_frame(raw_data)
        if eth_proto == 8:  # IPv4
            src_ip, dest_ip, proto, payload = ipv4_packet(data)
            print(f"\n[+] Packet captured")
            print(f"    Source IP      : {src_ip}")
            print(f"    Destination IP : {dest_ip}")
            print(f"    Protocol       : {proto}")
            print(f"    Payload        : {binascii.hexlify(payload[:40]).decode()}")
