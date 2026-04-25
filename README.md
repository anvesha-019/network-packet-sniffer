# Network Packet Sniffer

## Description
A Python-based packet sniffer built using Scapy to capture and analyze real-time network traffic.

## Features
- Captures TCP packets
- Extracts source & destination IP addresses
- Displays port numbers
- Logs packet data into a file
- Supports packet filtering

## Tools Used
- Python
- Scapy

## How It Works
The program uses Scapy's sniff() function to capture packets. Each packet is processed to extract IP and protocol information, which is then displayed and stored in a log file.

## How to Run
pip install scapy
python sniffer.py

## Output
<img width="877" height="239" alt="Screenshot 2026-04-25 194907" src="https://github.com/user-attachments/assets/2ac72721-dd67-4187-bd91-35621c59ef0b" />
<img width="1603" height="894" alt="Screenshot 2026-04-25 195036" src="https://github.com/user-attachments/assets/c01863e0-d6d0-4adb-a4fa-6a72497c86ad" />

