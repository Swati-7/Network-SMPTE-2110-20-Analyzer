# 🕵️‍♂️ Packet Sniffer Tool

## 📘 Description
This project is a simple packet sniffer tool developed in Python using raw sockets. It captures and analyzes incoming and outgoing packets on a network interface, displaying useful information such as:

- Source and Destination IP addresses
- Protocol types (TCP, UDP, ICMP, etc.)
- Payload data (in hexadecimal format)

> ⚠️ **Disclaimer:** This tool is intended strictly for educational and ethical use only. Unauthorized packet sniffing may violate privacy and local laws.

## ✨ Features
- Real-time packet capturing
- Protocol identification
- Payload data inspection
- Lightweight CLI interface

## 🧰 Technologies Used
- Python 3.x
- `socket`
- `struct`
- `os` (for permission handling)

## 🚀 Getting Started

### Prerequisites
- Python 3 installed
- Root/admin privileges required to run raw sockets

### Installation
```bash
git clone https://github.com/swati-7/packet-sniffer.git
cd packet-sniffer
pip install -r requirements.txt

